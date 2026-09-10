#  Matplotlib Module 

Matplotlib is a Python library used for **data visualization and plotting graphs**.

```python
import matplotlib.pyplot as plt
```

---

# 1. Basic Line Plot 

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.title("My Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
```

### Important syntax

```python
plt.plot(x, y)
plt.title("Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

---

# 2. Line Plot Formatting 

```python
plt.plot(x, y, color="red", linestyle="--", marker="o")
```

Common options:

```text
color / c       → line color
linestyle / ls  → line style
linewidth / lw  → line thickness
marker          → point style
markersize      → marker size
alpha           → transparency
```

Example:

```python
plt.plot(x, y, color="blue", linestyle="--",
         marker="o", linewidth=2, markersize=8)
```

---

# 3. Common Line Styles

```python
plt.plot(x, y, linestyle="-")    # solid
plt.plot(x, y, linestyle="--")   # dashed
plt.plot(x, y, linestyle=":")    # dotted
plt.plot(x, y, linestyle="-.")   # dash-dot
```

---

# 4. Markers 

```python
plt.plot(x, y, marker="o")
```

Common markers:

```text
o  → circle
s  → square
^  → triangle
*  → star
+  → plus
x  → x
.  → point
```

---

# 5. Multiple Lines 

```python
x = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [5, 15, 25, 35]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()
plt.show()
```

### `legend()`

Displays the names of different lines.

```python
plt.legend()
```

---

# 6. Grid 

```python
plt.grid()
```

Customize:

```python
plt.grid(axis="x")
plt.grid(axis="y")
```

---

# 7. X-Ticks and Y-Ticks 

Change the values displayed on axes:

```python
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 10, 20, 30, 40])
```

Custom labels:

```python
plt.xticks([1, 2, 3], ["A", "B", "C"])
```

---

# 8. Bar Chart 

```python
languages = ["Python", "Java", "C", "C++"]
students = [40, 25, 30, 20]

plt.bar(languages, students)

plt.title("Programming Language Students")
plt.xlabel("Languages")
plt.ylabel("Students")

plt.show()
```

### Horizontal Bar

```python
plt.barh(languages, students)
```

---

# 9. Scatter Plot 

Used to show the **relationship between two variables**.

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.scatter(x, y)

plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

Formatting:

```python
plt.scatter(x, y, alpha=0.5, marker="o")
```

---

# 10. Pie Chart 

```python
sizes = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels)

plt.title("Distribution")
plt.show()
```

Show percentage:

```python
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
```

---

# 11. Histogram 

Used to show **distribution of numerical data**.

```python
marks = [45, 50, 55, 60, 60, 65, 70, 75, 80]

plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
```

Change number of bins:

```python
plt.hist(marks, bins=5)
```

---

# 12. Subplots 

Used to create multiple plots in one figure.

```python
plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.subplot(2, 1, 2)
plt.bar(x, y)

plt.show()
```

### Syntax

```python
plt.subplot(rows, columns, position)
```

Example:

```text
subplot(2,1,1)

Graph 1
───────
Graph 2
───────

subplot(2,1,2)
```

---

# 13. Figure Size 

```python
plt.figure(figsize=(10, 5))
```

Example:

```python
plt.figure(figsize=(10, 5))

plt.plot(x, y)

plt.show()
```

---

# 14. Save Graph 

Instead of displaying the graph:

```python
plt.savefig("graph.png")
```

Recommended:

```python
plt.savefig("graph.png", dpi=300, bbox_inches="tight")
```

You can save as:

```text
.png
.jpg
.pdf
.svg
```

---

# 15. Axis Limits 

Set the range of axes:

```python
plt.xlim(0, 10)
plt.ylim(0, 100)
```

Example:

```python
plt.plot(x, y)

plt.xlim(0, 6)
plt.ylim(0, 40)

plt.show()
```

---

# 16. Text / Annotation 

Add text to a graph:

```python
plt.text(2, 20, "Important Point")
```

Basic annotation:

```python
plt.annotate("Highest",
             xy=(4, 30),
             xytext=(3, 35))
```

---

# 17. Add Horizontal / Vertical Lines 

Horizontal:

```python
plt.axhline(y=20)
```

Vertical:

```python
plt.axvline(x=3)
```

---

# 18. Tight Layout 

Prevents labels from overlapping:

```python
plt.tight_layout()
```

Usually used before:

```python
plt.show()
```

or:

```python
plt.savefig("graph.png", bbox_inches="tight")
```

---

# 19. Remove / Clear Plot

```python
plt.clf()      # clear entire figure
plt.cla()      # clear current axes
plt.close()    # close figure
```

---

# 20. Commonly Used Functions 

| Function             | Use                  |
| -------------------- | -------------------- |
| `plt.plot()`         | Line graph           |
| `plt.bar()`          | Bar chart            |
| `plt.barh()`         | Horizontal bar       |
| `plt.scatter()`      | Scatter plot         |
| `plt.pie()`          | Pie chart            |
| `plt.hist()`         | Histogram            |
| `plt.title()`        | Graph title          |
| `plt.xlabel()`       | X-axis label         |
| `plt.ylabel()`       | Y-axis label         |
| `plt.legend()`       | Show legend          |
| `plt.grid()`         | Show grid            |
| `plt.xticks()`       | X-axis ticks         |
| `plt.yticks()`       | Y-axis ticks         |
| `plt.xlim()`         | X-axis limits        |
| `plt.ylim()`         | Y-axis limits        |
| `plt.subplot()`      | Multiple plots       |
| `plt.figure()`       | Create/resize figure |
| `plt.savefig()`      | Save graph           |
| `plt.show()`         | Display graph        |
| `plt.tight_layout()` | Fix spacing          |

---





#   CHEAT SHEET

```python
import matplotlib.pyplot as plt

plt.plot(x, y)             # Line
plt.bar(x, y)              # Bar
plt.barh(x, y)             # Horizontal bar
plt.scatter(x, y)          # Scatter
plt.hist(data)             # Histogram
plt.pie(data)              # Pie

plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()
plt.grid()

plt.xticks(...)
plt.yticks(...)

plt.xlim(...)
plt.ylim(...)

plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)

plt.tight_layout()

plt.savefig("graph.png")

plt.show()
```

##  Remember the basic order

```python
import matplotlib.pyplot as plt

plt.figure()

plt.plot(x, y)

plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
```

