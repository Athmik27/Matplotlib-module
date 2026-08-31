 # SUB-PLOTS

import matplotlib.pyplot as plt

import numpy as np

print(plt.subplots(2,2))

# create an figure and axes 

figure, axes=plt.subplots(2,2) 
#create multiple plots in one figure.
# figure → the entire window/canvas containing all plots.
# axes → the individual plot areas.
# 2,2 is 2 row x 2 columns 
plt.show()

# showing different graphs in each sub-plots
x=np.array([1,2,3,4,5])
figure, axes=plt.subplots(2,2) 
axes[0,0].plot(x,x*2)
plt.show()

x=np.array([1,2,3,4,5])
figure, axes=plt.subplots(2,2) 
axes[0,1].plot(x,x**2)
# plt.show()

x=np.array([1,2,3,4,5])
figure, axes=plt.subplots(2,2) 
axes[1,0].plot(x,x*3)
plt.show()

x=np.array([1,2,3,4,5])
figure, axes=plt.subplots(2,2) 
axes[1,1].plot(x,x**3)
plt.show()