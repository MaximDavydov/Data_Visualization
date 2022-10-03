from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Create D6
die = Die()

# Make some rolls, and store results in a list.
# Делаем броски и сохраняем результаты
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
# Анализ результатов
# frequencies = dict()
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(*frequencies.items())

# Visualize the results.
# Визуализация результатов
# Создаем резульатыт для столбцов
x_values = list(range(1, die.num_sides+1))
# Bar - столбцовая диаграмма
data = [Bar(x=x_values, y=frequencies)]

# Заголовки осей - их просто вписываем в макет Layout
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# Возвращает объект, который задает макет и конфигурацию + заголовок
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis={'title': 'Result'}, yaxis=y_axis_config)
# Построение диаграммы - словарь в данными + название файла
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
