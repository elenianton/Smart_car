# Process tsv files to extract all required information

PYTHONIOENCODING=UTF-8 python3.8 local/test_data_prep.py 

src_data=utils
test_dir=data/test

spk2utt_test=$test_dir/spk2utt
utt2spk_test=$test_dir/utt2spk

$src_data/utt2spk_to_spk2utt.pl <$utt2spk_test >$spk2utt_test || exit 1

# Data validation

trans_test=$test_dir/text

utt2spk_test=$test_dir/utt2spk

# for test
ntrans_test=$(wc -l <$trans_test)
nutt2spk_test=$(wc -l <$utt2spk_test)
! [ "$ntrans_test" -eq "$nutt2spk_test" ] && \
  echo "Inconsistent #transcripts($ntrans_test) and #utt2spk($nutt2spk_test)" && exit 1;

$src_data/validate_data_dir.sh --no-feats $test_dir || exit 1;

echo "$0: successfully prepared data in $test_dir"

exit 0