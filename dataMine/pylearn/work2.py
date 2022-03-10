import numpy as np
import math

def EuclideanDistance(v1,v2):
    d=0
    for i in range(len(v1)):
        d1=(v1[i]-v2[i])**2
        d=d+d1
    return np.sqrt(d)

def ManhattanDistance(v1,v2):
    d=0
    for i in range(len(v1)):
        d1= abs(v1[i]-v2[i])
        d=d+d1
    return d

def MinkowskiDistance(v1,v2,q):
    d=0
    for i in range(len(v1)):
        d1=(v1[i]-v2[i])**q
        d=d+d1
    return pow(d, 1/q)
    
def LmaxDistance(v1,v2):
    d=0
    for i in range(len(v1)):
        d1= abs(v1[i]-v2[i])
        if d1>d:
            d=d1
    return d

v1=[22,1,42,10]
v2=[20,0,36,8]
print(EuclideanDistance(v1,v2))
print(ManhattanDistance(v1,v2))
print(MinkowskiDistance(v1,v2,3))
print(LmaxDistance(v1,v2))