import folium
map=folium.Map(location=[29.898699, 79.576839],zoom_start=6,tiles='OpenStreetMap')
#2. create a feature group
fg=folium.FeatureGroup(name="My Map")
#3.Now We are adding multiple marker in our single map using for loop 
for coordinates in([29.898699, 79.576839],[29.858699, 79.556839]):
    fg.add_child(folium.Marker(location=coordinates, popup="Hi,this is my home", tooltip=None, 
    icon=folium.Icon(color='blue', icon_color='white', icon='info-sign', angle=0, prefix='glyphicon'), draggable=False))
    
    # fg.add_child(folium.Marker(location=[29.898699, 79.576839], popup="Hi I am Pratibha ", tooltip=None, 
    # icon=folium.Icon(color='blue', icon_color='white', icon='info-sign', angle=0, prefix='glyphicon'), draggable=False))

#1. Adding Marker To our Map use folium.marker()
map.add_child(fg)
map.save("myhome.html")