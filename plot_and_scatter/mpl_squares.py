import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

input_values = list(range(1, 6))
squares = [num ** 2 for num in range(1, 6)]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

## Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
