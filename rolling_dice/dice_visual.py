from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Create D6
die_1 = Die()
die_2 = Die(10)


# Make some rolls, and store results in a list.
# Делаем броски и сохраняем результаты
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
# Анализ результатов
# frequencies = dict()
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(*frequencies.items())

# Visualize the results.
# Визуализация результатов
# Создаем резульатыт для столбцов
x_values = list(range(2, max_result+1))
# Bar - столбцовая диаграмма
data = [Bar(x=x_values, y=frequencies)]

# Заголовки осей - их просто вписываем в макет Layout
# dtick - помечает все деления
x_axis_config = {'title': 'Result', 'dtick': 0}
y_axis_config = {'title': 'Frequency of Result'}
# Возвращает объект, который задает макет и конфигурацию + заголовок
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', xaxis={'title': 'Result'}, yaxis=y_axis_config)
# Построение диаграммы - словарь в данными + название файла
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
