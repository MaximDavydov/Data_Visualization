import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

from die import Die

die1 = Die(6)
die2 = Die(6)

results = [die1.roll() * die2.roll() for _ in range(1000)]
frequence = [results.count(side) for side in range(1, (die1.num_sides * die2.num_sides) + 1)]

x = list(range(1, (die1.num_sides * die2.num_sides) + 1))

# make data:
# np.random.seed(3)
# x = 0.5 + np.arange(8)
# y = np.random.uniform(2, 7, len(x))
y = frequence

# plot
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(15, 5), dpi=60)

ax.bar(x, y, width=0.8, edgecolor="white", linewidth=0.9)

ax.set(xlim=(0, (die1.num_sides * die2.num_sides) + 1), xticks=np.arange(1, (die1.num_sides * die2.num_sides) + 1),
       ylim=(0, 300))

plt.show()