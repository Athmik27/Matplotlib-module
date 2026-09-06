# BAR CHARTS

import matplotlib.pyplot as plt

categories=['python','java','c++']
values=[15,10,25]

plt.bar(categories,values)
# # syntax 
#         # x → categories on X-axis
#         # height → values/heights of bars on y axis.
# plt.bar(x, height)

plt.show()

# HORIZONTAL BAR CHART
categories=['python','java','c++']
values=[15,10,25]

plt.barh(categories,values) # h -> horizontal

plt.show()
# plt.bar()    → Vertical
# plt.barh()   → Horizontal

# syntax
# plt.bar(x, y, width)

# Controls the inside color of the bars:
# plt.bar(x, height, color="red") for multiple we use color=["",""s]

# Controls the border color of the bars:
# plt.bar(x, height, edgecolor="black")

# linewidth
# Controls the thickness of the border.
# plt.bar(
#     x,
#     height,
#     edgecolor="black",
#     linewidth=2
# )
# Larger value → thicker border.

# align
# Controls how the bar is positioned relative to the X-axis location.
# Two common values:
# align="center"

# or

# align="edge"

# in center The bar is centered on the X position.
# plt.bar(x, height, align="center")

# alpha
# Controls transparency.
# plt.bar(x, height, alpha=0.5)
# Values are generally between:
# 0 → completely transparent
# 1 → completely opaque

# label
# Gives the bars a name for the legend.
# plt.bar(x, height, label="Students")
# plt.legend() legend is a small box that tells you what each color, line, or marker that represents

import matplotlib.pyplot as plt

x = ["Python", "Java", "C", "C++"]
y = [80, 60, 70, 50]

plt.bar(
    x,
    y,
    width=0.6,
    color="green",
    edgecolor="black",
    linewidth=1.5,
    alpha=0.8,
    label="Marks"
)

plt.xlabel("Programming Language")
plt.ylabel("Marks")
plt.title("Programming Language Marks")

plt.legend()
plt.show()