# HISTOGRAM

import matplotlib.pyplot as plt
import numpy as np

# scores=np.random.normal(loc=15,scale=10,size=10)
# loc=15	Mean (average) = 15
# scale=10	Standard deviation = 10
# size=10	Generate 10 numbers

# plt.hist(scores)
# plt.show()

#clip() method
#clip = set a limit/range.

# scores=np.random.normal(loc=15,scale=10,size=10)

# plt.hist(scores)
# scores = np.clip(scores,0,100)
# plt.show()

#np.clip(array, minimum, maximum) 

# bins function
scores=np.random.normal(loc=80,scale=10,size=100)

plt.hist(scores,bins=5)# bins means divide the range of scores into 5 groups
scores = np.clip(scores,0,100)
plt.show()

# color and outline color 

plt.hist(scores,
         bins=5,
         color='lightgreen',
         edgecolor='black')
plt.show()