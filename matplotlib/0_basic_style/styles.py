import matplotlib.pyplot as plt
import numpy as np

N_ROW = 2
N_COL = 2

fig, axes = plt.subplots(N_ROW, N_COL, figsize=(9, 9) )
x1 = np.linspace(0, 10, 10)
y1 = x1 ** 0.5
y12 = x1 ** 0.5 + 1
y13 = x1 ** 0.5 + 2

ax = axes[0][0]

ax.set_title("line")
ax.set_xlabel("Days")
ax.set_ylabel("Value")
ax.grid()
ax.plot(x1, y1, 'ro-')
ax.plot(x1, y12, 'b--')
ax.plot(x1, y13, 'g*-')

ax = axes[0][1]

ax.set_title("bar")
ax.set_xlabel("Days")
ax.set_ylabel("Value")
ax.bar(x1, y1)

ax = axes[1][0]

ax.set_title("scatter")
#plt.scatter(x1, y1 + np.random.random(len(y1)))
ax.scatter(x1, y1)

ax = axes[1][1]
ax.set_title("pie")
labels = 'A', 'B', 'C'
sizes = 15, 20, 50
colors = 'lightcoral', 'gold', 'lightskyblue'
explode = (0, 0.1, 0) # explode the 2nd one 0.1 space
ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow='True', startangle=50)

plt.show()