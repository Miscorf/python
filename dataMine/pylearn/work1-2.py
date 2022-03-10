import numpy as np
import matplotlib.pyplot as plt

data=[13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70]
print("（a）平均数：",np.mean(data))
print("中位数：",np.median(data))
counts = np.bincount(data)
#print(counts)
print("(b)众数：25和35，数据的模态为二模")
MidRange=(np.max(data)+np.min(data))/2
print("(c)中列数：",MidRange)
dataLen=len(data)
Q1=data[int((dataLen-0.5)*0.25) ]
Q3=data[int((dataLen-0.5)*0.75) ]
print("(d)Q1:",Q1)
print("Q3:",Q3)
IQR=Q3-Q1
MAX1=Q3+1.5*IQR
MIN2=Q1-1.5*IQR
print("(e)五数：")
print("最小观测值：",13,"中位数：",np.median(data),"Q1:",Q1,"Q3:",Q3,"最大观测值：",57.5)
plt.boxplot(data,labels="x")
plt.title("(f)盒图",fontproperties="SimHei")
plt.show()
