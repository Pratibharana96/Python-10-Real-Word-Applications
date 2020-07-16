import folium
import pandas as pd 
import json
import io

data_json = io.open("world.json",'r',encoding='utf-8-sig').read()
data = pd.read_csv('Volcanoes.txt')
# print(data)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# function for managing color 
def color_changer(elv):
    if elv < 1000:
        return 'green'
    elif elv <=3000:
        return 'orange'
    else:
        return 'red'
# print(lon)
map=folium.Map(location=[38.58, -99.09],zoom_start=6,tiles='OpenStreetMap')
#2. create a feature group
fgv=folium.FeatureGroup(name="Volcanoes")
#3.Now We are adding multiple marker in our single map using for loop 
for lt,ln,elv in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius= 6, popup=str(elv)+" m", tooltip=None, fill_color=color_changer(elv),fill_opacity= 0.7,color='grey',
    icon=folium.Icon(color=color_changer(elv), icon_color='white', icon='info-sign', angle=0, prefix='glyphicon')))
    
    # fg.add_child(folium.Marker(location=[29.898699, 79.576839], popup="Hi I am Pratibha ", tooltip=None, 
    # icon=folium.Icon(color='blue', icon_color='white', icon='info-sign', angle=0, prefix='glyphicon'), draggable=False))
# fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig'.read()))))
# fg.add_child(folium.GeoJson(data=data_json,
# style_function=lambda x: {"fillColour": "yellow"}))
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=data_json,style_function=lambda x: {'fillColor':'blue' if x['properties']
['POP2005'] < 10000000
else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else
'red' }))
# Adding Layer To our Map use folium.LayerControl

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("myhome.html")