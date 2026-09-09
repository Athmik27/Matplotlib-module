# PIE CHART

import matplotlib.pyplot as plt

categories=['python','java','c++','dart','go','rust']
values=[15,10,25,16,20,28]

plt.pie(values)
plt.show()

# Labels for pie chart
plt.pie(values,labels=categories)
plt.show()

Autopct function
plt.pie(values,
        labels=categories,
        autopct='%1.1f')
plt.show()

#Autopct func with % symbol
plt.pie(values,
        labels=categories,
        autopct='%1.1f%%')
plt.show()

# colors for the pie chart values

categories=['python','java','c++','dart','go','rust']
values=[15,10,25,16,20,28]
colors=["blue",'yellow','red','green','orange','brown']
plt.pie(values,colors=colors)
plt.show()


# EXPLODE THE pie chart
categories=['python','java','c++','dart','go','rust']
values=[15,10,25,16,20,28]
colors=["blue",'yellow','red','green','orange','brown']
plt.pie(values,
        colors=colors,
        explode=[0,0,0,0.2,0,0])
plt.show()

# add shadow to  pie chart
categories=['python','java','c++','dart','go','rust']
values=[15,10,25,16,20,28]
colors=["blue",'yellow','red','green','orange','brown']
plt.pie(values,
        colors=colors,
        explode=[0,0,0,0.2,0,0],
        shadow=True)
plt.show()

# add angle of rotation by startangle function
categories=['python','java','c++','dart','go','rust']
values=[15,10,25,16,20,28]
colors=["blue",'yellow','red','green','orange','brown']
plt.pie(values,
        colors=colors,
        explode=[0,0,0,0.2,0,0],
        shadow=True,
        startangle=90)
plt.show()
