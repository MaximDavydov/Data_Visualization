import csv
from datetime import datetime

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

filename = '/Users/maxim/python_work/Data_Visualization/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(head_row)

    # Вывод с индексами всех заголовков
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Reading maximum value
    highs, dates, lows = [], [], []
    for row in reader:
        high, low = int(row[5]), int(row[6])
        highs.append(high)
        lows.append(low)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

# print(highs)

# Plot the high temperatures.
# Задали тему
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 7))

#alpha - прозрачность фона
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title('Daily high and low temperatures – 2018', fontsize=24)
plt.xlabel('', fontsize=16)
# Вывод метки дат по диагонали
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
