import folium
import pandas

map = folium.Map(location=[40.75, -111.87], zoom_start=6)
data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'orange'
    elif 1000 <= elevation < 3000:
        return 'red'
    else:
        return 'darkred'

html = """
Name: 
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank" style="text-decoration: none"> %s</a><br>
Height: %s m
"""

fg = folium.FeatureGroup(name="My map")
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=70)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color=color_producer(el), fill_opacity=0.8))
map.add_child(fg)

map.save("Map1.html")