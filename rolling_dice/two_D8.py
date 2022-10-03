from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# создание Д8
die1 = Die(8)
die2 = Die(8)

results = list()
for roll in range(1000000):
    summ_rolls = die1.roll() + die2.roll()
    results.append(summ_rolls)

frequencies = list()
for summary in range(2, die1.num_sides + die2.num_sides + 1):
    frequencies.append(results.count(summary))

x_values = list(range(2, die1.num_sides + die2.num_sides + 1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Results of summary"}
y_axis_config = {"title": "Frequences"}

my_layout = Layout(title='Results of rolling two D8 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
