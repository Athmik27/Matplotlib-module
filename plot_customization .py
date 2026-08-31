import matplotlib.pyplot as plt

import numpy as np

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y)
plt.show()

# same we can use numpyarray for the above as its more efficient that the above method

x=np.array([2023,2024,2025])
y=np.array([15,20,25])
plt.plot(x,y)
plt.show()

# MARKER CONCEPT

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*')
plt.show()

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*',markersize='10')
plt.show()

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*',markersize='10',markerfacecolor="red")
plt.show()



x = [2023, 2024, 2025]
y = [15, 20, 25]

plt.plot(x, y)
plt.savefig("mygraph.png") # this is used to save the figure

print("Graph created successfully")


x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*',markersize='10',markerfacecolor="red",markeredgecolor="black")
plt.show()

# LINES CONCEPT

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*',markersize='10',markerfacecolor="red",markeredgecolor="black",linestyle="dashed")
plt.show()

#linestyle=doted,dashed,dashdot,solid,none(for no line)

#LINE WIDTH

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*',markersize=10,markerfacecolor="red",markeredgecolor="black",linestyle="dashed",linewidth=2)
plt.show()

#LINE COLOR

x=[2023,2024,2025]
y=[15,20,25]
plt.plot(x,y,marker='*',markersize=10,markerfacecolor="red",markeredgecolor="black",linestyle="dashed",linewidth=2,color="red")
plt.show()
# # for linr color we just use 'color'
 #     (or)
# INSTEAD OF WRITING ALL THE ABOVE TERMS WE CAN USE 'DICTIONARY'

x=[2023,2024,2025]
y=[15,20,25]
line_style=dict(marker='*',
                markersize=10,
                markerfacecolor="red",
                markeredgecolor="black",
                linestyle="dashed",
                linewidth=2,
                color="red")
plt.plot(x,y,**line_style)
plt.show()

