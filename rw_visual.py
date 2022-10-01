import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(num_points=10000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('ggplot')
fix, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15, c=rw.x_values, cmap=plt.cm.Blues)
plt.show()