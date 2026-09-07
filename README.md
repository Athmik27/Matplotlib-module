

## 1. What is Matplotlib?

**Matplotlib** is a Python library used to create **graphs, charts, and visualizations**.

It is commonly used with:

* NumPy
* Pandas
* Seaborn
* Scikit-learn

### Common graphs

* Line plot
* Scatter plot
* Bar chart
* Horizontal bar chart
* Histogram
* Pie chart
* Box plot
* Area plot
* Subplots

---

# 2. Basic Matplotlib Structure

The basic structure is:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y)

plt.title("My Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.savefig("graph.png")
```

### Mental model

Think of Matplotlib like this:

```text
Data
 ↓
Choose graph
 ↓
Customize graph
 ↓
Add title/labels
 ↓
Save/display graph
```

---

# 3. Line Plot

A line plot connects data points with lines.

### Syntax

```python
plt.plot(x, y)
```

### Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.savefig("line_plot.png")
```

---

# 4. Adding Title

Use:

```python
plt.title("My Graph")
```

Example:

```python
plt.plot(x, y)

plt.title("Student Marks")

plt.savefig("marks.png")
```

---

# 5. X-axis Label

Use:

```python
plt.xlabel("Label")
```

Example:

```python
plt.xlabel("Students")
```

---

# 6. Y-axis Label

Use:

```python
plt.ylabel("Label")
```

Example:

```python
plt.ylabel("Marks")
```

---

# 7. Complete Basic Graph

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [20, 40, 30, 50, 45]

plt.plot(x, y)

plt.title("Student Performance")
plt.xlabel("Student Number")
plt.ylabel("Marks")

plt.savefig("student_performance.png", bbox_inches="tight")
```

---

# 8. `plt.show()`

Normally:

```python
plt.show()
```

is used to display the graph.

Example:

```python
plt.plot(x, y)
plt.show()
```

If your environment has problems displaying the graph, you can save it instead:

```python
plt.savefig("graph.png")
```

For your setup, using `savefig()` is convenient.

---

# 9. `plt.savefig()`

Used to save a graph as an image.

### Syntax

```python
plt.savefig("filename.png")
```

Example:

```python
plt.plot(x, y)

plt.savefig("my_graph.png")
```

### Better version

```python
plt.savefig("my_graph.png", bbox_inches="tight")
```

`bbox_inches="tight"` helps prevent labels from being cut off.

---

# 10. Figure Size

To control the size of the graph:

```python
plt.figure(figsize=(10, 6))
```

Example:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)

plt.savefig("graph.png")
```

### Important

`figsize` is:

```text
(width, height)
```

and the unit is **inches**.

---

# 11. Common Mistake with `figsize`

❌ Wrong:

```python
plt.tight_layout(figsize=(10, 6))
```

`plt.tight_layout()` does **not** set figure size.

✅ Correct:

```python
plt.figure(figsize=(10, 6))

plt.plot(x, y)

plt.tight_layout()
```

---

# 12. Line Color

Use:

```python
plt.plot(x, y, color="red")
```

Example:

```python
plt.plot(x, y, color="red")
```

Short form:

```python
plt.plot(x, y, "r")
```

Common colors:

```text
"red"
"blue"
"green"
"black"
"orange"
"purple"
```

---

# 13. Line Style

Use:

```python
linestyle="--"
```

Examples:

```python
plt.plot(x, y, linestyle="-")
plt.plot(x, y, linestyle="--")
plt.plot(x, y, linestyle=":")
plt.plot(x, y, linestyle="-.")
```

Common styles:

```text
-     solid
--    dashed
:     dotted
-.    dash-dot
```

---

# 14. Line Width

Use:

```python
linewidth=3
```

Example:

```python
plt.plot(x, y, linewidth=3)
```

`linewidth` controls the thickness of the line.

---

# 15. Markers

Markers show individual data points.

Example:

```python
plt.plot(x, y, marker="o")
```

Common markers:

```text
o   circle
s   square
^   triangle
*   star
+   plus
x   x
.   point
```

Example:

```python
plt.plot(
    x,
    y,
    marker="o"
)
```

---

# 16. Marker Size

Use:

```python
markersize=10
```

Example:

```python
plt.plot(
    x,
    y,
    marker="o",
    markersize=10
)
```

---

# 17. Transparency — `alpha`

`alpha` controls transparency.

Range:

```text
0 → completely transparent
1 → completely visible
```

Example:

```python
plt.plot(x, y, alpha=0.5)
```

Use a numeric value:

```python
alpha=0.5
```

---

# 18. Grid

Add grid lines:

```python
plt.grid()
```

Example:

```python
plt.plot(x, y)

plt.grid()

plt.savefig("graph.png")
```

You can control the style:

```python
plt.grid(
    linestyle="--",
    alpha=0.5
)
```

---

# 19. Legend

A legend tells us what each line represents.

Example:

```python
plt.plot(x, y, label="Marks")

plt.legend()
```

Complete:

```python
plt.plot(x, y, label="Student Marks")

plt.title("Performance")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.legend()

plt.savefig("marks.png")
```

---

# 20. Multiple Lines

You can draw multiple lines on the same graph.

```python
x = [1, 2, 3, 4, 5]

python_marks = [60, 70, 80, 75, 90]
java_marks = [50, 65, 70, 80, 85]

plt.plot(x, python_marks, label="Python")
plt.plot(x, java_marks, label="Java")

plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()

plt.savefig("comparison.png")
```

---

# 21. X-axis Limits

Use:

```python
plt.xlim(start, end)
```

Example:

```python
plt.xlim(0, 10)
```

This controls the visible x-axis range.

---

# 22. Y-axis Limits

Use:

```python
plt.ylim(start, end)
```

Example:

```python
plt.ylim(0, 100)
```

---

# 23. Ticks

Ticks are the values shown along the axes.

### X ticks

```python
plt.xticks()
```

Example:

```python
plt.xticks([1, 2, 3, 4, 5])
```

### Y ticks

```python
plt.yticks()
```

Example:

```python
plt.yticks([0, 20, 40, 60, 80, 100])
```

---

# 24. Changing Tick Labels

Example:

```python
x = [1, 2, 3]
y = [50, 70, 90]

plt.plot(x, y)

plt.xticks(
    [1, 2, 3],
    ["Alice", "Bob", "Charlie"]
)

plt.savefig("students.png")
```

Now:

```text
1 → Alice
2 → Bob
3 → Charlie
```

---

# 25. Scatter Plot

A scatter plot displays individual points.

### Syntax

```python
plt.scatter(x, y)
```

Example:

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.scatter(x, y)

plt.savefig("scatter.png")
```

---

# 26. Scatter Plot with Transparency

```python
plt.scatter(
    x,
    y,
    alpha=0.5
)
```

---

# 27. Scatter Plot with Marker

```python
plt.scatter(
    x,
    y,
    marker="o"
)
```

---

# 28. Scatter Plot — Common Parameters

```python
plt.scatter(
    x,
    y,
    color="blue",
    marker="o",
    alpha=0.5,
    s=100
)
```

Important parameters:

| Parameter   | Meaning          |
| ----------- | ---------------- |
| `x`         | X values         |
| `y`         | Y values         |
| `color`     | Point color      |
| `marker`    | Point shape      |
| `alpha`     | Transparency     |
| `s`         | Point size       |
| `edgecolor` | Border color     |
| `linewidth` | Border thickness |

---

# 29. Bar Chart

A bar chart compares categories.

### Syntax

```python
plt.bar(x, height)
```

Example:

```python
subjects = ["Python", "Java", "C"]

marks = [90, 75, 80]

plt.bar(subjects, marks)

plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.savefig("bar.png")
```

---

# 30. Horizontal Bar Chart

Use:

```python
plt.barh()
```

Example:

```python
subjects = ["Python", "Java", "C"]
marks = [90, 75, 80]

plt.barh(subjects, marks)

plt.savefig("horizontal_bar.png")
```

### Difference

```python
plt.bar()
```

→ vertical

```python
plt.barh()
```

→ horizontal

---

# 31. Bar Width

```python
plt.bar(
    subjects,
    marks,
    width=0.5
)
```

`width` controls the width of vertical bars.

---

# 32. Bar Colors

```python
plt.bar(
    subjects,
    marks,
    color="green"
)
```

---

# 33. Histogram

A histogram shows the **distribution of numerical data**.

Example:

```python
marks = [45, 50, 55, 60, 62, 65, 70, 72, 75, 80]

plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.savefig("histogram.png")
```

---

# 34. Histogram Bins

`bins` determines how the values are grouped.

```python
plt.hist(
    marks,
    bins=5
)
```

Example:

```python
plt.hist(
    marks,
    bins=10
)
```

### Mental model

If:

```python
bins=5
```

the data is divided into approximately 5 groups.

---

# 35. Pie Chart

A pie chart represents proportions.

### Syntax

```python
plt.pie(values, labels=labels)
```

Example:

```python
subjects = ["Python", "Java", "C"]
marks = [50, 30, 20]

plt.pie(
    marks,
    labels=subjects
)

plt.savefig("pie.png")
```

---

# 36. Pie Chart Percentages

Use:

```python
autopct="%1.1f%%"
```

Example:

```python
plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)
```

This displays percentages.

---

# 37. Pie Chart — `explode`

`explode` separates slices from the center.

Example:

```python
explode = [0.1, 0, 0]

plt.pie(
    marks,
    labels=subjects,
    explode=explode
)
```

### Important error

If there are 3 slices:

```python
labels = ["Python", "Java", "C"]
```

then `explode` must also contain 3 values:

```python
explode = [0.1, 0, 0]
```

❌ Wrong:

```python
explode = [0.1, 0, 0, 0]
```

This causes:

```text
ValueError:
explode must be of length x
```

---

# 38. Pie Chart Start Angle

```python
plt.pie(
    marks,
    labels=subjects,
    startangle=90
)
```

`startangle` controls where the pie chart begins.

---

# 39. Box Plot

A box plot is used to understand:

* Distribution
* Median
* Quartiles
* Outliers

Example:

```python
marks = [45, 50, 55, 60, 62, 65, 70, 72, 75, 100]

plt.boxplot(marks)

plt.ylabel("Marks")

plt.savefig("boxplot.png")
```

---

# 40. Box Plot Important Concepts

A box plot contains:

```text
        |
    Maximum
        |
    ───────
       |
    ┌─────┐
    │     │
    │Median
    │     │
    └─────┘
       |
    ───────
        |
    Minimum
```

It helps identify **outliers**.

---

# 41. Area Plot

Use:

```python
plt.fill_between()
```

Example:

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.fill_between(x, y)

plt.savefig("area.png")
```

---

# 42. Text on Graph

Use:

```python
plt.text()
```

Example:

```python
plt.plot(x, y)

plt.text(
    3,
    15,
    "Important Point"
)

plt.savefig("text_graph.png")
```

Syntax:

```python
plt.text(x, y, "text")
```

---

# 43. Annotation

Use:

```python
plt.annotate()
```

Example:

```python
plt.plot(x, y)

plt.annotate(
    "Highest",
    xy=(5, 25)
)

plt.savefig("annotation.png")
```

Useful for pointing out important values.

---

# 44. `tight_layout()`

Used to automatically adjust spacing.

```python
plt.tight_layout()
```

Example:

```python
plt.figure(figsize=(10, 6))

plt.plot(x, y)

plt.title("My Graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()

plt.savefig("graph.png")
```

### Remember

```text
figsize → controls graph size
tight_layout() → controls spacing
```

---

# 45. Subplots

Subplots allow multiple graphs in one figure.

### Syntax

```python
plt.subplot(rows, columns, position)
```

Example:

```python
plt.subplot(2, 1, 1)

plt.plot(x, y)

plt.subplot(2, 1, 2)

plt.bar(x, y)

plt.savefig("subplots.png")
```

Meaning:

```text
2 → rows
1 → columns
1 → first graph
```

---

# 46. Modern Subplot Method

A more flexible approach is:

```python
fig, ax = plt.subplots()
```

Example:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y)

ax.set_title("My Graph")
ax.set_xlabel("X")
ax.set_ylabel("Y")

fig.tight_layout()

fig.savefig("graph.png")
```

### Important difference

Pyplot style:

```python
plt.plot()
plt.title()
plt.xlabel()
```

Object-oriented style:

```python
ax.plot()
ax.set_title()
ax.set_xlabel()
```

For beginners, learn `plt.*` first, then become comfortable with `fig, ax`.

---

# 47. Multiple Subplots with `subplots()`

Example:

```python
fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, y)
ax[0, 1].scatter(x, y)
ax[1, 0].bar(x, y)
ax[1, 1].plot(x, y)

fig.tight_layout()

fig.savefig("multiple_plots.png")
```

Layout:

```text
┌────────────┬────────────┐
│   Plot 1   │   Plot 2   │
├────────────┼────────────┤
│   Plot 3   │   Plot 4   │
└────────────┴────────────┘
```

---

# 48. Pandas + Matplotlib

Matplotlib is frequently used with Pandas.

Example:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample.csv")

plt.plot(
    df["Height"],
    df["Weight"]
)

plt.xlabel("Height")
plt.ylabel("Weight")

plt.savefig("height_weight.png")
```

---

# 49. NumPy + Matplotlib

Example:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)

y = x ** 2

plt.plot(x, y)

plt.savefig("numpy_plot.png")
```

---

# 50. Common Plot Types — When to Use What?

| Plot      | Use                                          |
| --------- | -------------------------------------------- |
| Line      | Trend over time/order                        |
| Scatter   | Relationship between two numerical variables |
| Bar       | Compare categories                           |
| Barh      | Horizontal category comparison               |
| Histogram | Distribution                                 |
| Pie       | Proportions                                  |
| Box plot  | Distribution + outliers                      |
| Area      | Magnitude/trend                              |
| Subplots  | Multiple graphs together                     |

---

# 51. Line Plot vs Scatter Plot

### Line plot

```python
plt.plot(x, y)
```

Used mainly for:

```text
Trend
Time series
Continuous data
```

### Scatter plot

```python
plt.scatter(x, y)
```

Used mainly for:

```text
Relationship
Correlation
Individual observations
```

---

# 52. Bar Chart vs Histogram

### Bar chart

Used for:

```text
Categorical data
```

Example:

```text
Python → 90
Java   → 80
C      → 70
```

### Histogram

Used for:

```text
Numerical data distribution
```

Example:

```text
Marks distribution
Age distribution
Height distribution
```

---

# 53. Axis Spines

**Spines** are the borders around the plotting area.

Conceptually:

```text
       Top spine
    ┌─────────────┐
    │             │
Left│    Graph    │Right
spine             spine
    │             │
    └─────────────┘
      Bottom spine
```

You can access them through an Axes object:

```python
fig, ax = plt.subplots()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
```

---

# 54. Matplotlib and Seaborn

Seaborn is built on top of Matplotlib.

So you can combine them:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(
    x=x,
    y=y
)

plt.title("My Graph")

plt.savefig("seaborn_graph.png")
```

This is important for Data Science.

---

# 55. Common Parameters You Should Know

### `color`

Controls color:

```python
color="red"
```

### `alpha`

Controls transparency:

```python
alpha=0.5
```

### `marker`

Controls marker shape:

```python
marker="o"
```

### `linewidth`

Controls line thickness:

```python
linewidth=2
```

### `linestyle`

Controls line style:

```python
linestyle="--"
```

### `label`

Name used in legend:

```python
label="Python"
```

### `figsize`

Controls figure size:

```python
figsize=(10, 6)
```

---

# 56. Complete Example

```python
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [70, 85, 60, 90, 75]

plt.figure(figsize=(10, 6))

plt.bar(
    students,
    marks,
    alpha=0.8
)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.ylim(0, 100)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "student_marks.png",
    bbox_inches="tight"
)
```

---

# 57. Important Matplotlib Functions

## Basic

```python
plt.plot()
plt.scatter()
plt.bar()
plt.barh()
plt.hist()
plt.pie()
plt.boxplot()
```

## Labels

```python
plt.title()
plt.xlabel()
plt.ylabel()
```

## Appearance

```python
plt.grid()
plt.legend()
plt.xlim()
plt.ylim()
plt.xticks()
plt.yticks()
```

## Figure

```python
plt.figure()
plt.subplot()
plt.subplots()
plt.tight_layout()
plt.savefig()
plt.show()
```

## Annotation

```python
plt.text()
plt.annotate()
```

---

# 58. Matplotlib Cheat Sheet

## Import

```python
import matplotlib.pyplot as plt
```

## Line

```python
plt.plot(x, y)
```

## Scatter

```python
plt.scatter(x, y)
```

## Bar

```python
plt.bar(x, y)
```

## Horizontal Bar

```python
plt.barh(x, y)
```

## Histogram

```python
plt.hist(data, bins=10)
```

## Pie

```python
plt.pie(values, labels=labels)
```

## Box Plot

```python
plt.boxplot(data)
```

## Title

```python
plt.title("Title")
```

## X Label

```python
plt.xlabel("X")
```

## Y Label

```python
plt.ylabel("Y")
```

## Grid

```python
plt.grid()
```

## Legend

```python
plt.legend()
```

## X limits

```python
plt.xlim(0, 100)
```

## Y limits

```python
plt.ylim(0, 100)
```

## X ticks

```python
plt.xticks()
```

## Y ticks

```python
plt.yticks()
```

## Figure size

```python
plt.figure(figsize=(10, 6))
```

## Tight layout

```python
plt.tight_layout()
```

## Save

```python
plt.savefig("graph.png")
```

## Display

```python
plt.show()
```

---

# 59. Most Important Syntax Pattern

Remember this pattern:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.plot(x, y)

plt.title("Title")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid()
plt.legend()

plt.tight_layout()

plt.savefig("graph.png")
```

You can adapt this structure to most basic Matplotlib problems.

---

# 60. Common Errors

## Error 1 — Wrong `figsize`

❌

```python
plt.tight_layout(figsize=(10, 6))
```

✅

```python
plt.figure(figsize=(10, 6))
plt.tight_layout()
```

---

## Error 2 — Wrong number of `explode` values

If you have:

```python
values = [30, 40, 30]
```

you need:

```python
explode = [0.1, 0, 0]
```

not:

```python
explode = [0.1, 0, 0, 0]
```

---

## Error 3 — Forgetting to import pyplot

❌

```python
plt.plot(x, y)
```

without importing.

✅

```python
import matplotlib.pyplot as plt
```

---

## Error 4 — Mismatched X and Y lengths

❌

```python
x = [1, 2, 3]
y = [10, 20]
```

These cannot be directly plotted together.

✅

```python
x = [1, 2, 3]
y = [10, 20, 30]
```

---

## Error 5 — Confusing `width` and `height`

For:

```python
plt.bar(x, height)
```

the second argument represents the **bar heights**.

For:

```python
plt.barh(y, width)
```

the second argument represents the **bar widths**.

---

# 61. Placement Priority

For interviews and Data Science, learn these first:

### MUST KNOW ⭐⭐⭐

```text
plt.plot()
plt.scatter()
plt.bar()
plt.barh()
plt.hist()

plt.title()
plt.xlabel()
plt.ylabel()

plt.legend()
plt.grid()

plt.xticks()
plt.yticks()

plt.figure(figsize=...)
plt.tight_layout()
plt.savefig()
```

### SHOULD KNOW ⭐⭐

```text
plt.pie()
plt.boxplot()
plt.xlim()
plt.ylim()
plt.subplot()
plt.subplots()
plt.text()
plt.annotate()
```

### Later / Advanced ⭐

```text
Object-oriented API
Advanced subplots
Custom tick formatters
Dates
Animations
Advanced styling
Transforms
```

---


```

---

#  Final Quick Revision

Before an interview, remember:

```python
import matplotlib.pyplot as plt
```

### Line

```python
plt.plot(x, y)
```

### Scatter

```python
plt.scatter(x, y)
```

### Bar

```python
plt.bar(x, y)
```

### Horizontal Bar

```python
plt.barh(x, y)
```

### Histogram

```python
plt.hist(data, bins=10)
```

### Pie

```python
plt.pie(values, labels=labels)
```

### Box Plot

```python
plt.boxplot(data)
```

### Title

```python
plt.title("Title")
```

### Labels

```python
plt.xlabel("X")
plt.ylabel("Y")
```

### Legend

```python
plt.legend()
```

### Grid

```python
plt.grid()
```

### Limits

```python
plt.xlim(0, 100)
plt.ylim(0, 100)
```

### Ticks

```python
plt.xticks()
plt.yticks()
```

### Figure Size

```python
plt.figure(figsize=(10, 6))
```

### Spacing

```python
plt.tight_layout()
```

### Save

```python
plt.savefig("graph.png")
```

### Display

```python
plt.show()
```

---

#  Final Matplotlib Checklist

Before moving to advanced visualization, make sure you can explain and use:

* [ ] `plt.plot()`
* [ ] `plt.scatter()`
* [ ] `plt.bar()`
* [ ] `plt.barh()`
* [ ] `plt.hist()`
* [ ] `plt.pie()`
* [ ] `plt.boxplot()`
* [ ] `plt.title()`
* [ ] `plt.xlabel()`
* [ ] `plt.ylabel()`
* [ ] `plt.legend()`
* [ ] `plt.grid()`
* [ ] `plt.xticks()`
* [ ] `plt.yticks()`
* [ ] `plt.xlim()`
* [ ] `plt.ylim()`
* [ ] `plt.figure(figsize=...)`
* [ ] `plt.tight_layout()`
* [ ] `plt.savefig()`
* [ ] `plt.subplot()`
* [ ] `plt.subplots()`
* [ ] `alpha`
* [ ] `marker`
* [ ] `color`
* [ ] `linewidth`
* [ ] `linestyle`
* [ ] `label`
* [ ] Axis spines
* [ ] Matplotlib + NumPy
* [ ] Matplotlib + Pandas
* [ ] Matplotlib + Seaborn

