# SCATTER GRAPH

import matplotlib.pyplot as plt

x=['python','java','c++','dart','go','rust']
y=[15,10,25,16,20,28]



plt.scatter(x,y,
            color="blue",
            alpha=0.5       # alpha Controls the transparency 
                            # alpha ranges from:
                            # 0   → completely transparent
                            # 0.5 → semi-transparent
                            # 1   → completely opaque
            )
plt.show()


plt.scatter(x,y,
            color="blue",
            alpha=0.5 ,
            s=100     # here s is size of scatterplot

            )
plt.show()

# plt.legend() shows us the scale of the graph