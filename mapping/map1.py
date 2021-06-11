import folium
import json
import pandas

data = pandas.read_csv("Volcanoes.csv")
lon = list(data["Longitude"])
lat = list(data["Latitude"])
elev = list(data["Elevation (m)"])
name = list(data["Volcano Name"])
vol_type = list(data["Type"])

world_file = open("world.json", "r", encoding='utf-8-sig')
world = json.load(fp=world_file)


def color_maker(ele):
    if ele < 2000:
        return 'green'
    elif ele < 3000:
        return 'orange'
    else:
        return 'red'


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m <br>
Type: %s
"""

map1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name, t in zip(lat, lon, elev, name, vol_type):
    iframe = folium.IFrame(
        html=html % (name, name, el, t),
        width=200,
        height=100)
    fgv.add_child(
        folium.CircleMarker(
            location=(lt, ln),
            radius=5,
            popup=folium.Popup(iframe),
            fill_color=color_maker(el),
            color='black',
            fill_opacity=0.8,
            weight=1
        )
    )

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=world,
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000
                             else 'yellow' if x['properties']['POP2005'] < 100000000
                             else 'orange' if x['properties']['POP2005'] < 1000000000
                             else 'red'})
              .add_child(folium.GeoJsonTooltip(data=world, fields=['POP2005'], aliases=["Population: "])))

map1.add_child(fgp)
map1.add_child(fgv)
map1.add_child(folium.LayerControl())
map1.keep_in_front(fgv)
map1.save("Map1.html")
