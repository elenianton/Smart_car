# Process tsv files to extract all required information

PYTHONIOENCODING=UTF-8 python3 local/process.py 


src_data=utils
dev_dir=data/dev
train_dir=data/train



spk2utt_dev=$dev_dir/spk2utt
utt2spk_dev=$dev_dir/utt2spk
spk2utt_train=$train_dir/spk2utt
utt2spk_train=$train_dir/utt2spk
$src_data/utt2spk_to_spk2utt.pl <$utt2spk_dev >$spk2utt_dev || exit 1
$src_data/utt2spk_to_spk2utt.pl <$utt2spk_train >$spk2utt_train || exit 1


# Data validation
trans_dev=$dev_dir/text
trans_train=$train_dir/text
utt2spk_dev=$dev_dir/utt2spk
utt2spk_train=$train_dir/utt2spk


# for dev
ntrans_dev=$(wc -l <$trans_dev)
nutt2spk_dev=$(wc -l <$utt2spk_dev)
! [ "$ntrans_dev" -eq "$nutt2spk_dev" ] && \
  echo "Inconsistent #transcripts($ntrans_dev) and #utt2spk($nutt2spk_dev)" && exit 1;

$src_data/validate_data_dir.sh --no-feats $dev_dir || exit 1;

echo "$0: successfully prepared data in $dev_dir"



# for train
ntrans_train=$(wc -l <$trans_train)
nutt2spk_train=$(wc -l <$utt2spk_train)
! [ "$ntrans_train" -eq "$nutt2spk_train" ] && \
  echo "Inconsistent #transcripts($ntrans_train) and #utt2spk($nutt2spk_train)" && exit 1;

$src_data/validate_data_dir.sh --no-feats $train_dir || exit 1;

echo "$0: successfully prepared data in $train_dir"

exit 0