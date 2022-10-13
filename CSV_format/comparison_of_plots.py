import csv
from datetime import datetime

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def get_weather_data(filename, highs, dates, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_index, high_index, low_index = header_row.index("DATE"), header_row.index("TMAX"), header_row.index("TMIN")
        place_name = ''
        for row in reader:
            if not place_name:
                place_name = row[header_row.index("NAME")]
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high, low = int(row[high_index]), int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                highs.append(((high - 32) * (5 / 9)))
                lows.append(((low - 32) * (5 / 9)))
                dates.append(current_date)

    return place_name

# Get weather data for Death Valley.
filename = '/Users/maxim/python_work/Data_Visualization/CSV_format/data/death_valley_2018_simple.csv'
highs, dates, lows = [], [], []
place_name = get_weather_data(filename, highs, dates, lows)

# Add Death Valley data to current plot.
# Plot the high temperatures.
# Задали тему
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(15, 7))

#alpha - прозрачность фона
ax.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)


# Get weather data for Sitka.
filename = '/Users/maxim/python_work/Data_Visualization/CSV_format/data/sitka_weather_2018_simple.csv'
highs, dates, lows = [], [], []
get_weather_data(filename, highs, dates, lows)
# Plot Sitka weather data.
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Get weather data for SanFr.
filename = '/Users/maxim/python_work/Data_Visualization/CSV_format/data/San_Franc_2019.csv'
highs, dates, lows = [], [], []
get_weather_data(filename, highs, dates, lows)
# Plot Sitka weather data.
plt.plot(dates, highs, c='purple', alpha=1)
plt.plot(dates, lows, c='black', alpha=1)
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.9)

# Format plot.
plt.title(f'Daily high and low temperatures – 2018\n{place_name}', fontsize=20)
plt.xlabel('', fontsize=16)
# Вывод метки дат по диагонали
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(-10, 60)


plt.show()