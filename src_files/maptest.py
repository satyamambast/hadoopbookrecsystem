#!/usr/bin/python3.8
import pickle
import sys
# inpfile=open("/home/satyam/hadoopbookrecsystem/src_file/input.txt",'r')
# word=inpfile.read().split(',')
word=sys.argv[1].split(",")
word=[x.strip() for x in word]
#print(word)    
#n = sys.argv[1]
inp=sys.stdin.readlines()
for i in inp:

    file=open(i.strip(),'rb')
    data=pickle.load(file)
    book_id=data["book_author"]+":sep:"+data["book_title"]
    total=data["book_total_count"]/1000.0
    relv=0
    for words in word:
        try:
            relv+=int(data[words])/total
        except KeyError:
            continue
    reducer=book_id+"\t"+str(relv)
    print(reducer)
#data=pickle.load(sys.stdin.buffer)
#print(len(data.keys()))