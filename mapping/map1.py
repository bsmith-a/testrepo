import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])


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
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(
        html=html % (name, name, el),
        width=200,
        height=100)
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Circle(color=color_maker(el))
        )
    )

map.add_child(fg)

map.save("Map1.html")
