# import csv
#
# filename = '/Users/maxim/python_work/Data_Visualization/data/death_valley_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)

import csv
from datetime import datetime

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

filename = '/Users/maxim/python_work/Data_Visualization/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(head_row)

    # Вывод с индексами всех заголовков
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Reading maximum value

    # Get dates, and high and low temperatures from this file.
    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high, low = int(row[4]), int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(((high - 32) * (5 / 9)))
            lows.append(((low - 32) * (5 / 9)))
            dates.append(current_date)

# print(highs)

# Plot the high temperatures.
# Задали тему
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(15, 7))

#alpha - прозрачность фона
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title('Daily high and low temperatures – 2018\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=16)
# Вывод метки дат по диагонали
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
