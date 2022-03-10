import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series


def load_data(x,y,a):
    data = pd.read_csv("dataMine\\data_train.csv")
    x = data.iloc[0:,0:-1]  # Series s.
    y = data.iloc[0:,-1]
    y = np.array(y)
    x = np.array(x)
    print("xlen",len(x))
    a = np.array([0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dtype='float64')
    return x,y,a
def model(a, b, x):
    c = np.dot(x,a)
    return c+b
def cost_function(a, b, x, y):
    return 0.5/n * (np.square(y-a*x-b)).sum()

def optimize(a,b,x,y):
    y_hat = model(a,b,x)
    da = ai()
    #print("da:",a[0]-alpha*da[0])
    db = (1.0/n) * ((y_hat-y).sum())
    for i in range(np.size(a)):
        a[i] = a[i] - alpha*da[i]
    b = b - alpha*db
    
    return a, b
def ai():
    y_hat = model(a,b,x)
    #print("yhat:",y_hat-y)
    da = np.array([])

    for i in range(np.size(a)):
        p=(y_hat-y)
        p=p*x[:,i]
        p=p.sum()
        p=(1.0/n)*p
        da = np.append(da,p)
        #da = np.append(da,(1.0/n) * ((y_hat-y)*x[:,i]).sum())
    return da

def iterate(a,b,x,y,times):
    for i in range(times):
        a,b = optimize(a,b,x,y)
        print(a,"b:",b)

    y_hat=model(a,b,x)
    return a,b

def ts(a,b):
    data = pd.read_csv("dataMine\\data_test.csv")
    x = data.iloc[0:,0:-1]  # Series s.
    y = data.iloc[0:,-1]
    y = np.array(y)
    x = np.array(x)
    y_hat = model(a,b,x)
    l = len(y)
    print("误差：",(1/n)*(np.square(y-y_hat)).sum())

def type_regerss(a,b):
    data = pd.read_csv("dataMine\\data_test.csv")
    x = data.iloc[0:,0:-1]  # Series s.
    y = data.iloc[0:,-1]
    y = np.array(y)
    x = np.array(x)
    l = len(y)
    y_hat = model(a,b,x)
    sum = 0.0
    for i in range(l):
        if y[i]>=6 and y_hat[i]>=6:
            sum = sum+1
        elif y[i]<6 and y_hat[i]<6:
            sum = sum+1
    print("分类准确率:", sum/l)

   
            

if __name__ == '__main__':
    x=[]
    y=[]
    b = 0
    a = np.array([0.0,0.0])
    alpha = 0.01

    x,y,a = load_data(x,y,a)
    x = [13854,12213,11009,10655,9503] #程序员工资，顺序为北京，上海，杭州，深圳，广州
    x = np.reshape(x,newshape=(5,1)) / 10000.0
    #print(x)
    y = [21332, 20162, 19138, 18621, 18016] #算法工程师，顺序和上面一致
    y = np.reshape(y,newshape=(5,1)) / 10000.0

    a = [0]
    n = len(x[0])
    a,b = iterate(a,b,x,y,50)
    plt.scatter(x,y)
    y_hat = model(a,b,x)
    plt.plot(x,y_hat)
    plt.show()
    ts(a,b)
    type_regerss(a,b)
