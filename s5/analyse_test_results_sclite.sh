hypothesis_tra=exp/tri3b/decode_tgmed_test/scoring/16.1.0.tra

ref_trw=exp/tri3b/decode_tgmed_test/scoring/test_filt.txt

cat $hypothesis_tra | utils/int2sym.pl -f 2- exp/tri3b/graph_tgmed/words.txt | sed s:\<UNK\>::g > 16.1.0_results.trw


python trw_to_wsj.py $hypothesis_tra 16.1.0_results.wsj
python trw_to_wsj.py $ref_trw ref.wsj

/opt/kaldi/tools/sctk/bin/sclite -i wsj -r ref.wsj -h 16.1.0_results.wsj -o dtl