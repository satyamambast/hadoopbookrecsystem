#!/bin/bash
hdfs namenode -format -y
/home/satyam/hadoop/sbin/start-dfs.sh
/home/satyam/hadoop/sbin/start-yarn.sh
hdfs dfs -mkdir /bookrec
hdfs dfs -put /home/satyam/hadoopbookrecsystem/src_files/log.txt /bookrec/log