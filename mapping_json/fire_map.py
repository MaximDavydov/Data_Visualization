import csv
from datetime import datetime


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

num_rows = 10000

filename = '/Users/maxim/python_work/Data_Visualization/mapping_json/data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    row_num = 0

    dates, brights, lats, lons, hover_text = [], [], [], [], []

    latitude, longitude, brightness, date_index = header_row.index("latitude"), header_row.index("longitude"), header_row.index("brightness"), header_row.index("acq_date")
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        brights.append(float(row[brightness]))
        label = f"{current_date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(current_date)
        lats.append(row[latitude])
        lons.append(row[longitude])
        hover_text.append(label)

        row_num += 1
        if row_num == num_rows:
            break


# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [br/20 for br in brights],
        # По какому списку раскидывать цвет
        'color': brights,
        # Тема
        'colorscale': 'rainbow',
        # Переворачивает шкалу
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]
my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')




