import glob
import sys
import os.path
import csv

test_dir = "./data/test"

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

with open('./data/test/wav.scp', 'wt', encoding='utf8', newline='') as wav_scp:
    tsv_writer = csv.writer(wav_scp, delimiter=' ',quotechar=' ')   
    paths = glob.glob('./wavdata/*/*.wav')
    z = {}
    for path in paths:
        wav_path=os.path.basename(path)
        id=wav_path.strip(".wav")
        #tsv_writer.writerow([id, path])
        z[id]=path
    dic_z = z.items()
    sorted_z = sorted(dic_z)
    for z in sorted_z:
        tsv_writer.writerow([z[0],z[1]])
    

#write utt2spk for all data
with open('./data/test/utt2spk', 'wt', encoding='utf8', newline='') as utt2spk:
    utt2spk_writer = csv.writer(utt2spk,  quotechar=' ', delimiter=' ', lineterminator='\n')
    all_paths = glob.glob('./wavdata/*/*.wav')
    
    a_list = []
    for path in all_paths:
        id_path = os.path.basename(path)
        id= id_path.strip(".wav")
        a_list += [id]
        sorted_list = sorted(a_list)
    
    for i in sorted_list:
        spk = i[0:5]
        utt2spk_writer.writerow([i, spk])

#write trans for all data
with open('./data/test/text', 'wt', encoding='utf8', newline='') as text_file:
    trans_writer = csv.writer(text_file, quotechar=' ', delimiter=' ', lineterminator='\n')
    trans_file = './wavdata/trans.trans'
    
    with open(trans_file, 'rt', encoding='UTF-8',) as f:
        reader=csv.reader(f, delimiter='\t')
        x={}
        
        for row in reader:
            full_id = os.path.basename(row[0])
            trans_id = full_id.strip(".wav")
            text = row[1]
            x[trans_id]= text
            
            
        
        dict_x=x.items()
        sorted_x=sorted(dict_x)
        for x in sorted_x:
            trans_writer.writerow([x[0],x[1]])        