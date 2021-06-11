import folium
import json
import pandas

# opens volcano file and reads longitude, latitude, elev, name, and type
data = pandas.read_csv("Volcanoes.csv")
lon = list(data["Longitude"])
lat = list(data["Latitude"])
elev = list(data["Elevation (m)"])
name = list(data["Volcano Name"])
vol_type = list(data["Type"])

# opens and stores world file
world_file = open("world.json", "r", encoding='utf-8-sig')
world = json.load(fp=world_file)


# chooses color for markers based on elevation
def color_maker(ele):
    if ele < 2000:
        return 'green'
    elif ele < 3000:
        return 'orange'
    else:
        return 'red'


# html code for volcano popups
# shows name, link to google search for the volcano, height, and type
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m <br>
Type: %s
"""

# creates map object
map1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
# creates feature group for volcano layer
fgv = folium.FeatureGroup(name="Volcanoes")

# makes volcano markers
for lt, ln, el, name, t in zip(lat, lon, elev, name, vol_type):
    # creates iframe to use html code
    iframe = folium.IFrame(
        html=html % (name, name, el, t),
        width=200,
        height=100)
    # sets location, size, color, and text of popups
    # iframe used for text
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

# creates feature group for population layer
fgp = folium.FeatureGroup(name="Population")

# adds children to population layer for each country
# library automatically draws polygons for each country
# fill color determined by population
fgp.add_child(folium.GeoJson(data=world,
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000
                             else 'yellow' if x['properties']['POP2005'] < 100000000
                             else 'orange' if x['properties']['POP2005'] < 1000000000
                             else 'red'})
              # adds tooltip to show population
              .add_child(folium.GeoJsonTooltip(data=world, fields=['POP2005'], aliases=["Population: "])))

# adds feature groups to map
map1.add_child(fgp)
map1.add_child(fgv)
# adds layer control panel to map
map1.add_child(folium.LayerControl())
# sets volcano layer to be always in front
map1.keep_in_front(fgv)
# generates html file
map1.save("Map1.html")
