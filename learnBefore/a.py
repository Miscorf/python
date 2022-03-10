import re
list_output=[]
b=['<http:','85','963']
def match_list(list_str):
    flag=1
    a=[]
    for item in list_str:
        if flag==2:
            flag=flag+1
            a.append(item)
            continue
        if re.match('<http:', item) != None:
            item = 'C:' + item
            a.append(item)
        elif re.match('^\d', item):
            item = 'G:' + item
            a.append(item)
        elif re.match('MESH:', item) != None:
            item = 'D:' + item
            a.append(item)
        elif (re.match('OMIM:', item) != None):
            item = 'D:' + item
            a.append(item)
        elif (re.match('D', item) != None and re.match('D:MESH', item) == None):
            item = 'D:MESH:' + item
            a.append(item)
        else:
            a.append(item)
        flag=flag+1
        if flag==4:
            flag=1
    return a


import pandas as pd
from pandas import read_csv
import re
import numpy as np
import csv
tsv_read=read_csv('D:\Mis\project\python\data.tsv', sep="\t")
array_data=np.array(tsv_read)
list_data=array_data.tolist()
list_output=[]
for item in list_data:
    for item1 in item:
        item1=item1.split(',')
        list_output.append(match_list(item1))
df = pd.DataFrame(list_output,columns=['ent1','rel','ent2'])
write_tvs('D:\Mis\project\python\data3.tsv',df)
