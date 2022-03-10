import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

age = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,61]
fat = [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,23.9,35.7]

#scatter plot
plt.plot(age,fat,'ro')
plt.xlabel("age")
plt.ylabel("%fat")
#plt.show()

# q-q plot    
x_ticks = np.arange(0, 100, 20)
y_ticks = np.arange(0, 100, 20)   
plt.scatter(x=age, y=fat, color='blue') 
plt.xlim((0, 100)) 
plt.ylim((0, 100))
plt.show()
