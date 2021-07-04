import subprocess
import sys

wordlist = sys.argv[1]
output_file = sys.argv[2]
pron_dict = {'θ':'T',                             
'ð':'D',
'ɣ':'G',
'j':'J',
'ɡ':'g',
'ɲ':'N',
'ŋ':'G',
'ɹ':'r',
'ʃ':'s',
'ç':'x',
'a':'A',
'ʌ':'A',
'ɛ':'E',
'e':'E',
'ɪ':'i',
'ʎ':'l',
'ɔ':'o',
'ʊ':'u'}

unknown_path = './local/unknown_words.txt'

with open(wordlist, 'r', encoding='UTF-8') as wlist:
   with open(output_file, 'a') as ofile:
      with open(unknown_path, 'r') as unknown_list:
         output = subprocess.run(["phonemize", "-l", "el",  unknown_path, "-o", "pron.txt"], universal_newlines = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         with open('pron.txt', 'r') as pron:
            list_word = []
            list_pron = []
            for u in unknown_list:
               if not u.isspace():
                  u = u.rstrip()
                  list_word+=[u]
            for i in pron:
               i = i.rstrip()
               i = " ".join(i)
               for key, value in pron_dict.items():
                  i = i.replace(key, value)
               list_pron += [i]     
            
               
            x= zip(list_word, list_pron)
            for t in x:
               space=" \t "
               ofile.write("{} {} {}\n".format(t[0], space, t[1]))
                        