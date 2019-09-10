import folium
import pandas
from folium.plugins import MarkerCluster


# Cities of World
city_data = pandas.read_csv("cities.csv")
city_lat = list(city_data["lat"])
city_lon = list(city_data["lng"])
city_name = list(city_data["city"])
map = folium.Map(location = [22.085867, 79.589589], zoom_start= 5, tiles="Stamen Terrain")
Cities = MarkerCluster(name= "Cities")
for tlt, tln, tnm in zip(city_lat, city_lon, city_name):
        Cities.add_child(folium.Marker(location = [tlt, tln], popup = tnm, icon = folium.Icon(color = "blue")))


# Capitals of Country
capitals_data = pandas.read_csv("capitals.csv")
capital_lat = list(capitals_data["Latitude"])
capital_lon = list(capitals_data["Longitude"])
capital_name = list(capitals_data["Capital"])
country_name = list(capitals_data["Country"])
Capitals = MarkerCluster(name = "Capitals")
for clt, cln, canm, conm in zip(capital_lat, capital_lon, capital_name, country_name):
        Capitals.add_child(folium.CircleMarker(location = [clt, cln], popup = str(canm) + ", " +str(conm), fill_color = "gray",color = "gray", fill_opacity="0.7"))


# World Population
popn = folium.FeatureGroup(name = "Population")
popn.add_child(folium.GeoJson(data =open("world.json","r",encoding="utf-8-sig" ).read(), style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 1000000 else 'yellow' if x['properties']['POP2005'] < 2000000 else 'red'}))


map.add_child(Cities)
map.add_child(Capitals)
map.add_child(popn)
map.add_child(folium.LayerControl())

map.save("Map1.html")
