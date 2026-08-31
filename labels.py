#TITLE

import matplotlib.pyplot as plt
x=[2023,2024,2025]
y=[15,20,25]
plt.title("CLASS SIZE")
line_style=dict(marker='*',
                markersize=10,
                markerfacecolor="red",
                markeredgecolor="black",
                linestyle="dashed",
                linewidth=2,
                color="red")
plt.plot(x,y,**line_style)
plt.show()


#FONTSIZE
x=[2023,2024,2025]
y=[15,20,25]
plt.title("CLASS SIZE",
          fontsize=5)
line_style=dict(marker='*',
                markersize=10,
                markerfacecolor="red",
                markeredgecolor="black",
                linestyle="dashed",
                linewidth=2,
                color="red")
plt.plot(x,y,**line_style)
plt.show()


#FONTSTYLE

x=[2023,2024,2025]
y=[15,20,25]
plt.title("CLASS SIZE",
          fontsize=5,
          family="Arial")
line_style=dict(marker='*',
                markersize=10,
                markerfacecolor="red",
                markeredgecolor="black",
                linestyle="dashed",
                linewidth=2,
                color="red")
plt.plot(x,y,**line_style)
plt.show()

#FONTWEIGHT
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
plt.plot(x,y,**line_style)
plt.show()


#FONT COLOR
x=[2023,2024,2025]
y=[15,20,25]
plt.title("CLASS SIZE",
          fontsize=5,
          family="Arial",
          fontweight='bold',
          color="Cyan")
line_style=dict(marker='*',
                markersize=10,
                markerfacecolor="red",
                markeredgecolor="black",
                linestyle="dashed",
                linewidth=2,
                color="red")
plt.plot(x,y,**line_style)
plt.show()


#VALUE FOR X AXIS
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
plt.xlabel("Years")
plt.plot(x,y,**line_style)
plt.show()


#VALUE FOR Y AXIS
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
plt.ylabel("Profit")
plt.plot(x,y,**line_style)
plt.show()


#VALUE FOR X AXIS WITH OTHER REQUIREMENTS
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
plt.xlabel("Years",
           fontsize=5,
           family="Arial",
           fontweight='bold')
plt.plot(x,y,**line_style)
plt.show()


#VALUE FOR Y AXIS WITH OTHER REQUIREMENTS
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
plt.ylabel("Profit",
            fontsize=5,
            family="Arial",
            fontweight='bold')
plt.plot(x,y,**line_style)
plt.show()


# X-TICKS FUNCTION FOR X AXIS
#plt.xticks() is used to control the values/labels shown on the X-axis of your graph

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
plt.xlabel("Years",
           fontsize=5,
           family="Arial",
           fontweight='bold')
plt.xticks(x)
plt.plot(x,y,**line_style)
plt.show()

#Y-TICKS FUNCTION FOR Y AXIS
# plt.yticks() is used to control the values/labels shown on the Y-axis of your graph.

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
plt.yticks(x)
plt.plot(x,y,**line_style)
plt.show()

#MODIFY THE TICKS FUNCTION
# axis can be 'x' or 'y'
plt.ticks_params(axis='both',
                 color='cyan'
                 )
