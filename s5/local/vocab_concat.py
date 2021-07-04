import os
import sys

vocabfull = sys.argv[1]
wordlist ='./local/wordlist.txt'

with open(vocabfull,'a',encoding='utf-8') as vocabfull:
    with open(wordlist,'r', encoding='utf-8') as wordlist:
        for word in wordlist: 
            vocabfull.write(word)
            
            

        