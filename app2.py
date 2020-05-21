import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
<h3>Volcano name:</h3>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def color_pro(elevation):
    if(elevation < 1000):
        return 'green' 
    elif (elevation >=1000 and elevation < 3000):
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name = "Volcanoes")
 
for lat, lon, elev, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius= 8, popup=folium.Popup(iframe), icon = folium.Icon(color = color_pro(elev)),
    fill_color = color_pro(elev), color = 'black', fill_opacity= .7))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <=x['properties']['POP2005'] < 20000000  else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map_html_popup_advanced.html")