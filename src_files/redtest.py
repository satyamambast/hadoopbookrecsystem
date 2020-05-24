#!/usr/bin/python3.8
import sys
inp=sys.stdin.readlines()
most_relevant=[[0,0] for x in range(5)]
for i in inp:
    i=i.strip()
    if(len(i)>=5):
        relev=i.split("\t")
        if len(relev)==1:
            print(relev)
            continue
        #print(relev)
        try:
            relev[1]=float(relev[1])
        except ValueError:
            continue
        if most_relevant[0][1]<relev[1]:
            most_relevant[0]=relev
            for i in range(1,5):
                if most_relevant[i-1][1]>most_relevant[i][1]:
                    most_relevant[i-1],most_relevant[i]=most_relevant[i],most_relevant[i-1]
                else:
                    break
            
for i in most_relevant[::-1]:
    print(i)