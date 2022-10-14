import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    # indent - отступы в 4 пробела
    json.dump(all_eq_data, f, indent=4)

all_eq_dict = all_eq_data['features']
print(len(all_eq_dict))
mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dict:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']["coordinates"][0]
    # lat = eq_dict['geometry']["coordinates"][1]
    # title = eq_dict['properties']["title"]
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']["coordinates"][0])
    lats.append(eq_dict['geometry']["coordinates"][1])
    hover_text.append(eq_dict['properties']["title"])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5 * mag for mag in mags],
        # По какому списку раскидывать цвет
        'color': mags,
        # Тема
        'colorscale': 'Rainbow',
        # Переворачивает шкалу
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
