#!/usr/bin/python3.8
import pickle
import sys
#inp=sys.stdin
#a=open('/home/satyam/hadoopbookrecsystem/new.txt','w+')
data=pickle.load(sys.stdin.buffer)
print(len(data.keys()))