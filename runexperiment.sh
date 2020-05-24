#!/bin/bash
mapred streaming -input /bookrec/log -output /bookrec/output -mapper "/home/satyam/hadoopbookrecsystem/src_files/maptest.py '$1'" -reducer /home/satyam/hadoopbookrecsystem/src_files/redtest.py
hdfs dfs -cat /bookrec/output/part-00000 > /home/satyam/hadoopbookrecsystem/top5books.txt
hdfs dfs -rm -r /bookrec/output