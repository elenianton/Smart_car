#!/usr/bin/env bash
source new_env/bin/activate


. ./cmd.sh
. ./path.sh

stage=0
. utils/parse_options.sh

set -euo pipefail


mkdir -p data 
# Data preparation
if [ $stage -le 1 ]; then
  bash local/greek_data_prep_test.sh 
  bash utils/combine_data.sh data/all data/train data/dev data/test
  bash local/prepare_lm_test.sh --data data/test --locdata data/local/lm_test

  utils/prepare_lang.sh data/local/dict_nosp \
    "<UNK>" data/local/lang_tmp_nosp_test data/lang_nosp_test

  bash local/greek_format_lms.sh --src-dir data/lang_nosp_test data/local/lm_test
      
fi 



if [ $stage -le 2 ]; then
  mfccdir=mfcc_test
  
  steps/make_mfcc.sh --cmd "$train_cmd" --nj 10 data/test exp/make_mfcc/test $mfccdir
  steps/compute_cmvn_stats.sh data/test exp/make_mfcc/test $mfccdir
  


  # Get the shortest 500 utterances first because those are more likely
  # to have accurate alignments.
  utils/subset_data_dir.sh --shortest data/train 500 data/train_500short
fi


# Now we compute the pronunciation and silence probabilities from training data,
# and re-create the lang directory.
if [ $stage -le 7 ]; then
  steps/get_prons.sh --cmd "$train_cmd" \
    data/train data/lang_nosp exp/tri3b
  utils/dict_dir_add_pronprobs.sh --max-normalize true \
    data/local/dict_nosp \
    exp/tri3b/pron_counts_nowb.txt exp/tri3b/sil_counts_nowb.txt \
    exp/tri3b/pron_bigram_counts_nowb.txt data/local/dict

  utils/prepare_lang.sh data/local/dict \
    "<UNK>" data/local/lang_tmp data/lang
  
  bash local/greek_format_lms.sh --src-dir data/lang data/local/lm_test

  steps/align_fmllr.sh --nj 5 --cmd "$train_cmd" \
    data/train data/lang exp/tri3b exp/tri3b_ali_train
fi

if [ $stage -le 8 ]; then
  # Test the tri3b system with the silprobs and pron-probs.

  # decode using the tri3b model
  utils/mkgraph.sh data/lang_test_tgmed \
                   exp/tri3b exp/tri3b/graph_tgmed
  for test in test; do
    steps/decode_fmllr.sh --nj 6 --cmd "$decode_cmd" \
                          exp/tri3b/graph_tgmed data/$test \
                          exp/tri3b/decode_tgmed_$test
    steps/lmrescore.sh --cmd "$decode_cmd" data/lang_test_test_tgmed \
                       data/$test exp/tri3b/decode_tgmed_$test
    # steps/lmrescore_const_arpa.sh \
    #   --cmd "$decode_cmd" data/lang_test_{tgsmall,tglarge} \
    #   data/$test exp/tri3b/decode_{tgsmall,tglarge}_$test
  done

  for x in exp/*/decode*; do [ -d $x ] && [[ $x =~ "$1" ]] && grep WER $x/wer_* | utils/best_wer.sh; done

fi
