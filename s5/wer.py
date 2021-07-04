import glob
import os

all_paths = glob.glob('./exp/tri3b/decode_tgmed_dev/*')
scores = {}
for path in all_paths:
    if 'wer' in path:
        name=os.path.basename(path)
        with open (path, 'r') as file:
            content = file.readlines()[1]
            scores[name] = content
            
x = scores.items()

for item in x:
    print (item[0], ":", item[1], '\n')

        