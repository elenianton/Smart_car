# Auto-generates the pronunciations for the words,

general_lexicon=/other/users/dimikon/asr-tts-class-2021/asr-recipes/cv_greek/s5/Greek400k.dictionary
wordlist=/other/users/dimikon/asr-tts-class-2021/asr-recipes/cv_greek/s5/data/local/lm/vocab-full.txt
output_file=final_dict.txt

PYTHONIOENCODING=UTF-8 python3 local/prepare.dict.py $general_lexicon $wordlist $output_file


