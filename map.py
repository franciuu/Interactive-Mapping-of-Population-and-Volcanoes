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

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=70)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color=color_producer(el), fill_opacity=0.8))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig')).read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000  
                                                      else 'orange' if x['properties']['POP2005'] < 20000000
                                                      else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")