from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die1 = Die(6)
die2 = Die(6)

results = []
for _ in range(1000):
    results.append(die1.roll() * die2.roll())
    
frequence = []
for side in range(1, (die1.num_sides * die2.num_sides) + 1):
    frequence.append(results.count(side))

x_values = list(range(1, (die1.num_sides * die2.num_sides) + 1))
# Создаем диаграмму
data = [Bar(x=x_values, y=frequence)]

x_axis_config = {'title': 'Reslut of summary'}
y_axis_config = {'title': 'Frequences'}

my_layout = Layout(title='Results of multiply rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='multiplication_two_D6.html')
