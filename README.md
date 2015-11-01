# Data Incubator Project Proposal

I am proposing an app that would rank various transportation systems in a city, based on various factors, such as financial cost, travel time and pollution index. An ideal place for this app, would be the webpage of a municipality, helping each resident of the city to choose the transportation system that suits them best , based on their priorities (money, time or environmental friendliness). Ideally, this information will be gathered based on past data and extrapolated to the future so that the app can predict these factors for a few coming years. 

The input going into the program would be the personalized travel schedule of the user. More precisely, the GPS location of their residence and the GPS locations of a few destinations they travel to on a regular basis. The app's output would be for example, the travel time or the cost predictions over the course of the next few years for each mode of transport.  

For the current proposal, I focus on the case of "vehicles". I would like to show how data on Taxis can be analyzed with the goal of predicting the time of travel with vehicle between any two points in New York city (Manhattan). 

## The Data

The data I will be using for my preliminary exploratory analysis can be found [here](https://uofi.app.box.com/NYCtaxidata). It has been originally obtained by [Dan Work](https://publish.illinois.edu/dbwork/open-data/) from the [New York City Taxi and Limousine Comission](http://www.nyc.gov/html/tlc/html/home/home.shtml). The raw data contains information on about 700 million taxi trips and takes up about 116GB in text CSV format. Due to the large size of the data, it is not present in this respository. Therefore, to run the programs presented here, you need to download the CVS tables, name them appropiately and put them in this directory with the rest of the files.


## Taxi GPS Coordinates

The first question to ask is whether the data is useful, for example in order to predict the time it takes to go from point A to point B in Manhattan. In other words, it is important to ask whether the data covers the GPS coordinates we are intersted in. I wrote a Python code which is [here](\Taxi_Map_NYC.py) in this repsoitory that reads the data and plots the GPS coordinates of the taxi pick-up and drop-off locations for a sub-sample of the data on top of [Google Maps](https://maps.google.ca/). The code uses [Pygmaps](https://code.google.com/p/pygmaps/), a Python wrapper for Google Maps JavaScript API V3. Pygmaps provides functions to generate HTML file which shows your GPS data on Google map. 

The outputs of the code are two html files called [pickup_map.html](\pickup_map.html) and [dropoff_map.html](\dropoff_map.html), which take time to load as each contain 10000 points plotted on top of Google maps.

You can see the GPS MAP it [here](https://raw.githubusercontent.com/fkamiab/data_incubator_project/master/GPS_MAP.png).




.. image:: /Histogram_Hour.png

http://htmlpreview.github.io/?https://github.com/fkamiab/data_incubator_project/blob/master/mymap.html
