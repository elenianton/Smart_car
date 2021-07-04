import glob
import sys
import os.path
import csv

dev_dir = "./data/dev"
train_dir = "./data/train"

if not os.path.exists(dev_dir):
    os.mkdir(dev_dir)
if not os.path.exists(train_dir):
    os.mkdir(train_dir)

with open('./data/wav_scp_file', 'wt', encoding='utf8', newline='') as wav_scp:
    tsv_writer = csv.writer(wav_scp, delimiter=' ', quotechar=' ')   
    paths = glob.glob('/data/logotypografia_subset/cd*/wavdata/*/*.wav')
    
    z = {}
    for path in paths:
        wav_path=os.path.basename(path)
        id=wav_path.strip(".wav")
        #tsv_writer.writerow([id, path])
        z[id]=path
    dic_z = z.items()
    sorted_z = sorted(dic_z)
    for z in sorted_z:
        tsv_writer.writerow([z[0],"sph2pipe -f wav {} |".format(z[1])])
    

#write trans for all data
with open('./data/trans_file', 'wt', encoding='utf8', newline='') as text_file:
    trans_writer = csv.writer(text_file, delimiter=' ')
    trans_paths = glob.glob('/data/logotypografia_subset/cd*/cd*.trans')
    
    for file in trans_paths:
        with open(file, 'rt', encoding='ISO-8859-7',) as f:
            reader=csv.reader(f, delimiter='\t')
            for row in reader:
                full_id = os.path.basename(row[0])
                trans_id = full_id.strip(".wav")
                text = row[1]
                trans_writer.writerow([trans_id, text])

#write utt2spk for all data
with open('./data/utt2spk_file', 'wt', encoding='utf8', newline='') as utt2spk:
    utt2spk_writer = csv.writer(utt2spk, delimiter=' ')
    all_paths = glob.glob('/data/logotypografia_subset/cd*/wavdata/*/*.wav')
    
    a_list = []
    for path in all_paths:
        id_path = os.path.basename(path)
        id= id_path.strip(".wav")
        a_list += [id]
        sorted_list = sorted(a_list)
    
    for i in sorted_list:
        spk = i[0:5]
        utt2spk_writer.writerow([i, spk])

#split tsv

def split_file(src_file, train_file, dev_file):
    src = open(src_file, "r")
    train = open(train_file, "wt")
    dev = open(dev_file, "wt")
    split = 1762
    line = 1
    line_reader = src.readline()
    while line_reader:
        if line <= split:
            dev.write(line_reader)
        else:
            train.write(line_reader)
        line += 1
        line_reader = src.readline()
    dev.close()
    train.close()     

# split utt2spk 
src_utt2spk = './data/utt2spk_file'
train_utt2spk = './data/train/utt2spk'
dev_utt2spk = './data/dev/utt2spk'

split_file(src_utt2spk, train_utt2spk, dev_utt2spk)

# split wav_scp
src_wav_scp = './data/wav_scp_file'
train_wav_scp = './data/train/wav.scp'
dev_wav_scp = './data/dev/wav.scp' 

split_file(src_wav_scp, train_wav_scp, dev_wav_scp)

#create text files for dev and train
with open('./data/train/text', 'wt', encoding='utf8') as trans_train:
    with open('./data/dev/text', 'wt', encoding='utf8') as trans_dev:
        with open('./data/train/utt2spk', 'r', encoding = 'utf8') as utt2spk_train:
            with open('./data/trans_file', 'r', encoding = 'utf8') as trans_gen:
                train_writer = csv.writer(trans_train, quotechar=' ', delimiter=' ', lineterminator='\n')
                dev_writer = csv.writer(trans_dev, quotechar=' ', delimiter=' ', lineterminator='\n')
                utt2spk_reader = csv.reader(utt2spk_train, delimiter = ' ')
                trans_gen_reader = csv.reader(trans_gen, delimiter = ' ')
                c = 0
                id_list = []
                x = {}
                y = {}
                for line in utt2spk_reader:
                    idd = line[0]
                    id_list += [idd]
                for tline in trans_gen_reader:
                    trans_id = tline[0]                    
                    transcr = tline[1]
                    text = transcr.replace("\r\n", "\n").replace("\r", "\n")
                    #text = "Testing" 
                    if trans_id in id_list:
                        x[trans_id]=text
                    else:
                        y[trans_id]=text
                       
                dic_x = x.items()
                sorted_x = sorted(dic_x)
                dic_y = y.items()
                sorted_y = sorted(dic_y)

                for x in sorted_x:
                    train_writer.writerow([x[0],x[1]])
                
                for y in sorted_y:
                    dev_writer.writerow([y[0],y[1]])

                
