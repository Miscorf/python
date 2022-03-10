import re
# 普通的匹配方式
ret = re.match( "嫦娥2号","嫦娥1号发射成功")
print(ret)
if(ret==None):
    print("yes")
#print(ret.group())

def write_csv_file(path, head, data):
    try:
        with open(path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='\t')
 
            if head is not None:
                writer.writerow(head)
 
            for row in data:
                writer.writerow(row)
 
            print("Write a CSV file to path %s Successful." % path)
    except Exception as e:
        print("Write an CSV file to path: %s, Case: %s" % (path, e))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_csv_write_tsv(path,tsv_read):
    with open(path,'w',newline='') as write_csv:
        write_csv.write(tsv_read.to_csv(sep='\t',index=False))

import pandas as pd
from pandas import read_csv
import re
import numpy as np
import csv
tsv_read=read_csv('D:\Mis\project\python\data.tsv', sep="\t")
print(tsv_read)
read_csv_write_tsv("D:\Mis\project\python\data3.tsv",tsv_read)
# with open("D:\Mis\project\python\data2.tsv",'w',newline='') as f_output:
#     tsv_output=csv.writer(f_output,delimiter='\t')
#     for row in tsv_read:
#         tsv_output.writerow(row)

# with open('D:\Mis\project\python\data2.tsv','w',newline='',encoding='utf-8') as f:
#     # tsv_w = csv.writer(f,lineterminator='\n')
#     tsv_test = csv.writer(f)
#     for row in tsv_read:
#         tsv_test.writerow(row)

