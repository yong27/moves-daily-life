#!/usr/bin/env python
import pickle
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

lifeblks, activities = pickle.load(open('summarized-life.pickle'))
#lifeblks, activities = pickle.load(open('summarized-weekdays-life.pickle'))
#lifeblks, activities = pickle.load(open('summarized-weekend-life.pickle'))
activity_colors = [
    ('home', '#dfddd4'),
    ('work', '#c1b58e'),
    ('eat', '#003851'),
    ('park', '#90b090'),
    ('library', '#db0000'),
    ('cafe', '#dbeed4'),
    ('shopping', '#4c441e'),
    ('hospital', '#4b92e1'),
    ('etc', '#dbeeee'),
    ('transport', '#306db0'),
    ('tour', '#eedbc1'),
]

activity_array = np.array([[actprops.get(act, 0.) for act, _ in activity_colors]
                           for blki, actprops in lifeblks]).transpose()

x = np.arange(activity_array.shape[1])
y_stack = np.cumsum(activity_array, axis=0)   # a 3x10 array

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(111)

actnames = []
colors = []
for i, (actname, color) in enumerate(activity_colors):
    if i == 0:
        ax1.fill_between(x, 0, y_stack[i, :], facecolor=color, edgecolor='#707070')
    else:
        ax1.fill_between(x, y_stack[i-1, :], y_stack[i, :], facecolor=color, edgecolor='#707070')
    actnames.append(actname)
    colors.append(color)

#ax1.legend(colors, actnames)

plt.ylim(0, 1)
plt.xlim(0, y_stack.shape[1])
plt.xticks(np.arange(0, y_stack.shape[1] + 1, 3 * 60 / 5))
ax1.set_xticklabels(range(0, 25, 3))
ax1.xaxis.set_minor_locator(MultipleLocator(12))
plt.grid(True, alpha=0.5)
plt.grid(True, which='minor', alpha=0.5)
plt.show()

