import numpy as np
a=[200,300,400,600,1000]
def maxmin(max,min,new_max,new_min,a):
    return (a-min)/(max-min)*(new_max-new_min)+new_min    
def zz(x,a,s):
    return (a-x)/s
def mad(a):
    s=0
    for item in a:
        s=s+abs(item-np.mean(a))
    return s/len(a)
for item in a:
    print(item)
    print("(a)最小最大规范化",maxmin(1000,200,1,0,item))
    print("(b)z规范化",zz(np.mean(a),item,np.std(a)))
    print("(c)z规范化绝对偏差",zz(np.mean(a),item,mad(a)))
    print("(d)小数偏差",item/10000)
