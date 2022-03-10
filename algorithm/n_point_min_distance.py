import numpy as np
import math

def distance(a,b):
    c = (a[0]-b[0])**2+(a[1]-b[1])**2
    c = math.sqrt(c)
    res.append([a, b, c])
    return c
def load_data():
    file=open("dataMine\da.txt")    
    p=[]
    c=[]
    for line in file.readlines():  
        ch = line[0:1]
        a=float(line[2:5])
        b=float(line[7:10])
        p.append((a,b,ch))
    print("p:",p)
    return p

# p = [(1.1, 2.0), (3.1, 1.0), (4.4, 5.3), (2.6, 3.2), (2.6, 4.6), (5.3, 5.2), (3.2, 4.5), (5.3, 4.7)]
# res=[]

def minDistance(P,l,h):
    max = math.inf
    if h - l <= 3:
        for i in range(l,h ):
            for j in range(i + 1, h):
                d = distance(p[i], p[j])
                if d < max:
                    max = d
        return max   
    else:
        mid = (h - l) // 2 + l
        axis = p[mid]
        
        d_left = minDistance(p, l, mid)
        d_right = minDistance(p, mid + 1, h)
        delta = min(d_left, d_right)  
        
        Y = sorted(p, key=lambda point: point[1])
        T = []
        #求中间部分的点，如果y坐标差值比递归求得的小则将其保存
        for i in range(len(Y)):  
            if abs(Y[i][0] - axis[0]) <= delta:
                T.append(Y[i])
                # k = k + 1
        delta_ = delta

        #中间部分点求最小
        for i in range(len(T)):
            if T[i][0]<mid:#Ti在mid左边
                for j in range(i + 1, min(i + 8, len(T))):
                    if abs(T[j][1]-T[i][1])<delta:   #Tj与Ti的y值相差不过delta时，进行判断是否最小
                        d = distance(T[i], T[j])
                        if d < delta:
                            delta_ = d
    return delta_
res = []
p = load_data()
md = minDistance(p, 0, len(p))
sres = sorted(res, key=lambda b: b[2])[0]
print("最小点对和最小距离",sres)


        
    