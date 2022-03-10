a= ['<http://bio2rdf.org/drugbank:DB00001>,ddi-interactor-in,<http://bio2rdf.org/drugbank:DB02123>']
c='<http://bio2rdf.org/drugbank:DB00001>,ddi-interactor-in,<http://bio2rdf.org/drugbank:DB02123>'
b=c.split(',')
#b 为list， c为字符串
print("打印b")
print(b)
import re
list_output=[]
a=1
for item in b:
    if a==2:
        a=a+1
        continue
    if re.match('<http:',item)!=None:
        item='C:'+item
        print("处理的每个都打印")
        print(item)
        list_output.append(item)
    elif re.match('MESH:',item)!=None:
        item='D:'+item
        list_output.append(item)
    else:
        list_output.append(item)
    a=a+1
    if(a==4):
        a=1
print("打印list——output：")
print(list_output)
        
        