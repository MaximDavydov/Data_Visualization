import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x_vals = list(range(1, 5000))
y_vals = [num ** 3 for num in x_vals]
y_vals5 = [num ** 3.2 for num in x_vals]

# Стиль окна
plt.style.use = 'bbplot'
# Создание фигуры и чертежей
fix, ax = plt.subplots()

# Генерация графика точек по параметрам + цветовая палитра + размер
ax.scatter(x_vals, y_vals, s=10, c=x_vals, cmap=plt.cm.flag)
ax.scatter(x_vals, y_vals5, s=10, c=y_vals, cmap=plt.cm.Blues)


# Название графика
ax.set_title('Cubes Numbers', fontsize=24)
# Х сторона и размер
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubes Values', fontsize=14)
# Деления на осях + шрифт
ax.tick_params(axis='both', which='major', labelsize=14)


# Диапазон по значениям
# ax.axis([0, 1100, 0, 110000])

# Авто-Сохранение графика
# plt.savefig('Cube_numbers.png', bbox_inches='tight')
plt.show()
