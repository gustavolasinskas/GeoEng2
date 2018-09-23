import pylab
import matplotlib.style
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# data
anual1 = 2400*12
anual2 = 3000*12

# axes
x1 = np.array(range(70))
y1 = np.array(x1*anual1)

x2 = np.array(range(5, 75))
y2 = np.array(x1*anual2)

for i in range(len(y1)):
    if y1[i+5] - y2[i] < 0:
        plt.plot(x2[i], y2[i], 'ro', label='Turning Point: %s years' %(i+5))
        break

# style
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

plt.title("Steve's Retirement", fontsize=20)
mpl.rc('lines', linewidth=1.5)
plt.ylabel('USD', fontsize=14)

plt.xlabel('Years', fontsize=14)
# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)

# Customize the grid
ax.grid(linestyle='-', linewidth='0.2', color='green')

plt.style.use('ggplot')

# ploting
plt.plot(x1, y1, label='Retire 2021')
plt.plot(x2, y2, label='Retire 2026')

pylab.xlim([0, 60])
pylab.ylim([0,2000000])
plt.legend()
plt.show()
