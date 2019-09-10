Application 2: Webmap

Features:
- displays different cities of world on map with marker
- displays capital of countries in circle marker
- displays name of location in popup
- colour codes different countries according to their population with choropleth map
- clusters or expands markers on map for accessibility of user
- toggles different features with a toggle window on top left

Additional Files:
1] world.json   : contains list of countries and their statistical data from 2005 of which their geographical coordinates and population are used
2] capitals.csv : contains list of capitals of countries along with their co-ordinates (latitude and longitude)
3] cities.csv   : contains list of few major cities of world along with their co-ordinates

Generated File:
1] Map1.html: this file is generated as output when main program is executed.

Libraries:
folium : to generate basemap, save final html file and  add different child groups from MarkerCluster and FeatureGroup
pandas : to read different csv files

Childrens of Folium:
Cities       : to plot major world cities from cities.csv
Capitals     : to plot capital of each country from capitals.csv
popn         : to colourcode different countries depending on their total population
LayerControl : to provide a checkbox which facilitates user to toggle visibility of other child

How to use:
1] Download capitals.csv, cities.csv, world.json and Ver1.py in same folder
2] Install Python 3 
3] In windows, open command prompt in current folder and type python Ver1.py
4] In linux, open terminal in current directory and type python3 Ver1.py
5] Open the generated html file
6] If folium or pandas error is displayed, install the libraries using following command on terminal:
			pip install folium
			pip install pandas