import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dataAge=[23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
dataFat=[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

ageMean=np.mean(dataAge)
fatMean=np.mean(dataFat)
ageMedian=np.median(dataAge)
fatMedian=np.median(dataFat)
ageStd=np.std(dataAge)
fatStd=np.std(dataFat)
print("(a)")
print("均值:age",ageMean,"fat",fatMean)
print("中位数:age",ageMedian,"fat",fatMedian,)
print("标准差:age",ageStd,"fat",fatStd)


plt.boxplot(dataAge,labels="x")
plt.title("age盒图",fontproperties="SimHei")
plt.show()
plt.boxplot(dataFat,labels="x")
plt.title("fat盒图",fontproperties="SimHei")
plt.show()
stats.probplot(dataAge, dist="norm", plot=plt)
plt.show()