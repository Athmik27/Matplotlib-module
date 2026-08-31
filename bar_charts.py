# BAR CHARTS

import matplotlib.pyplot as plt

# categories=['python','java','c++']
# values=[15,10,25]

# plt.bar(categories,values)
# # syntax 
#         # x → categories on X-axis
#         # height → values/heights of bars
# #plt.bar(x, height)

# plt.show()

# HORIZONTAL BAR CHART
categories=['python','java','c++']
values=[15,10,25]

plt.barh(categories,values) # h -> horizontal

plt.show()
# plt.bar()    → Vertical
# plt.barh()   → Horizontal