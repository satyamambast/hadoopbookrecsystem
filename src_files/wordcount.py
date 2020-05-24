import csv
import re
import string
import time
import nltk
import pickle
import os
path ='/home/satyam/test_bin/input'
output='/home/satyam/test_bin/output'
def txttobinary(book,log_file):
    document_text = open(os.path.join(path,book), 'r')
    newname=os.path.join(output,os.path.splitext(book)[0]+'.bin')
    log_file.write(newname)
    log_file.write("\n")
    st=time.time()
    frequency = {}
    flag=0
    text_string = document_text.read().lower()
    document_text.close()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
    x=-50
    while True:
        last=text_string[x::]
        if 'author' in last and 'title' in last:
            break
        x=x-10
    #print(last)
    auth_pattern = re.findall(r'author:.*', last)[0][7:]
    title_pattern = re.findall(r'title:.*', last)[0][6:]
    print(auth_pattern,"    ",title_pattern)

    stemmer = nltk.stem.SnowballStemmer("english")
    for word in match_pattern:    
        word=stemmer.stem(word.lower().translate(string.punctuation))
        count = frequency.get(word,0)
        frequency[word] = count + 1
        flag+=1
    frequency['book_title']=auth_pattern
    frequency['book_author']=title_pattern
    frequency['book_total_count']=flag
    new_document=open(newname,'wb+')
    pickle.dump(frequency,new_document,protocol=pickle.HIGHEST_PROTOCOL)
    new_document.close()
    print(len(frequency.keys()))
    # frequency_list = sorted(frequency.keys())

    # for words in frequency_list:
    #     print(words,frequency[words])
    end=time.time()
    print(flag)
    print(end-st)
log_file=open(os.path.join(output,"log.txt"),"w+")
for r, d, f in os.walk(path):
    for file in f:
        txttobinary(file,log_file)
log_file.close()
