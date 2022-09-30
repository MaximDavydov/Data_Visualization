import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [num ** 2 for num in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

# num_list_2 = list(range(0, 10000, 23))
#
# ax.plot(num_list_2, linewidth=3)
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.rainbow)


# Set chart title and label axes.
# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
# Назначение размера и шрифта на осях.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_scatter.png', bbox_inches='tight')
plt.show()
