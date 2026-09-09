# BAR CHARTS

import matplotlib.pyplot as plt

categories = ['python', 'java', 'c++']
values = [15, 10, 25]

plt.bar(categories, values)

# Syntax

# x → categories on X-axis

# height → values/heights of bars on Y-axis

# plt.bar(x, height)

plt.show()

# HORIZONTAL BAR CHART

categories = ['python', 'java', 'c++']
values = [15, 10, 25]

plt.barh(categories, values)  # h → horizontal

plt.show()

# plt.bar()    → Vertical

# plt.barh()   → Horizontal

# Syntax

# plt.bar(x, height, width)

# Controls the inside color of the bars:

# plt.bar(x, height, color="red")

# For multiple bars:

# color=["red", "blue", "green"]

# Controls the border color of the bars:

# plt.bar(x, height, edgecolor="black")

# linewidth

# Controls the thickness of the border.

# plt.bar(

# x,

# height,

# edgecolor="black",

# linewidth=2

# )

# Larger value → thicker border.

# align

# Controls how the bar is positioned relative to the X-axis location.

#

# Two common values:

# align="center"

# align="edge"

#

# center → The bar is centered on the X position.

# plt.bar(x, height, align="center")

# alpha

# Controls transparency.

# plt.bar(x, height, alpha=0.5)

#

# Values are generally between:

# 0 → completely transparent

# 1 → completely opaque

# label

# Gives the bars a name for the legend.

# plt.bar(x, height, label="Students")

# plt.legend()

#

# legend is a small box that tells you what each color,

# line, or marker represents.

# COMPLETE BAR CHART EXAMPLE

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
