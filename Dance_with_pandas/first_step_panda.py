import numpy
import pandas
import pandas as pd

csv_path = '/Users/maxim/python_work/Data_Visualization/CSV_format/data/moscow_2021_full.csv'

readed_data = pd.read_csv(csv_path, nrows=1)

print(readed_data)

s = {"STATION": "RSM00027612", "NAME": "MOSCOW, RS", "DATE": "2020-10-22",
     "PRCP": "6.9", "SNWD": '', "TAVG": "6.6", "TMAX": "4.8", "TMIN": "2.5"}

s = pd.Series(s)

s['Mach'] = 'Double'

print(s.index)

# s.drop(axes=2)

# print(s.labels)

s.to_csv('csv_data.csv')


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['X', 'Y', 'Z'])
print(df)

data = {'Name': ["Max", "Leo", "Vika", 'Martin', 'Mileo'],
        'Age': [10, 15, 20, 40, 50],
        'Address': ['Moscow', 'Nepal', 'Oiiter', "Roma", 'Chili'],
        'Qual': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'f'])
print(df)

df = pd.read_csv(csv_path, sep=',', header = None, nrows=10)
print(df)

print(df.head(3))
print(df.tail(4))