import folium
import pandas as pd 

data = pd.read_csv('Volcanoes.txt')
# print(data)
lat = list(data["LAT"])
lon = list(data["LON"])
# print(lon)
map=folium.Map(location=[38.58, -99.09],zoom_start=6,tiles='OpenStreetMap')
#2. create a feature group
fg=folium.FeatureGroup(name="My Map")
#3.Now We are adding multiple marker in our single map using for loop 
for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Hi,this is my home", tooltip=None, 
    icon=folium.Icon(color='blue', icon_color='white', icon='info-sign', angle=0, prefix='glyphicon')))
    
    # fg.add_child(folium.Marker(location=[29.898699, 79.576839], popup="Hi I am Pratibha ", tooltip=None, 
    # icon=folium.Icon(color='blue', icon_color='white', icon='info-sign', angle=0, prefix='glyphicon'), draggable=False))

#1. Adding Marker To our Map use folium.marker()
map.add_child(fg)
map.save("myhome.html")