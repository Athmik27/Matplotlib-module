# GRIND FUNCTION
import matplotlib.pyplot as plt

x=[2023,2024,2025]
y=[15,20,25]
plt.title("CLASS SIZE",
          fontsize=5,
          family="Arial",
          fontweight='bold')
line_style=dict(marker='*',
                markersize=10,
                markerfacecolor="red",
                markeredgecolor="black",
                linestyle="dashed",
                linewidth=2,
                color="red")
plt.ylabel("Years",
           fontsize=5,
           family="Arial",
           fontweight='bold')
plt.grid(axis='both',
        linestyle="dashed",
        linewidth=2,
        color="red") # axis='x' and axis='y'
plt.plot(x,y,**line_style)
plt.show()



