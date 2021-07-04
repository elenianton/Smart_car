import sys
import subprocess
import re
 
general_lexicon = sys.argv[1]
wordlist = sys.argv[2]
output_file = sys.argv[3]
 
with open(general_lexicon, encoding="utf-8") as lex:
    with open(wordlist, encoding="utf-8") as wlist:
        with open(output_file, 'w', encoding="utf-8") as ofile:
            
            
            gen_lex = {}   
            a_list = []         
            
            for line in lex:
                cline = line.rstrip()
                line_info = cline.split(" ")
                word = line_info[0]
                pronunciation = " ".join(line_info[1:])
                
                if word in gen_lex:
                    a_list.append(pronunciation)
                    gen_lex[word] = a_list
                else:   
                    a_list = [pronunciation]
                    gen_lex[word] = a_list
            
            b_list = []
            
            for line in wlist:
                
                a_word = line.rstrip()
                a_word = re.sub(r'[^\w\s]', '', a_word)

                if a_word in gen_lex:
                    for pron in gen_lex[a_word]:
                        ofile.write("{} {}\n".format(a_word, pron))
                else:
                    b_list += [a_word]

                    unknown_path = './local/unknown_words.txt'
                    
                    with open(unknown_path, 'w', encoding="utf-8") as unknown:
                        for w in b_list:
                            unknown.write("{}\n".format(w))
