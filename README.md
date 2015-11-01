# Data Incubator Project Proposal

I am proposing an app that would rank various transportation systems in a city, based on various factors, such as financial cost, travel time and pollution index. An ideal place for this app, would be the webpage of a municipality, helping each resident of the city to choose the transportation system that suits them best , based on their priorities (money, time or environmental friendliness). Ideally, this information will be gathered based on past data and extrapolated to the future so that the app can predict these factors for a few coming years. 

The input going into the program would be the personalized travel schedule of the user. More precisely, the GPS location of their residence and the GPS locations of a few destinations they travel to on a regular basis. The app's output would be for example, the travel time or the cost predictions over the course of the next few years for each mode of transport.  

For the current proposal, I focus on the case of "vehicles". I would like to show how data on Taxis can be analyzed with the goal of predicting the time of travel with vehicle between any two points in New York city (Manhattan). 

## The Data

The data I will be using for my preliminary exploratory analysis can be found [here](https://uofi.app.box.com/NYCtaxidata). It has been originally obtained by [Dan Work](https://publish.illinois.edu/dbwork/open-data/) from the [New York City Taxi and Limousine Comission](http://www.nyc.gov/html/tlc/html/home/home.shtml). The raw data contains information on about 700 million taxi trips and takes up about 116GB in text CSV format. Due to the large size of the data, it is not present in this respository. Therefore, to run the programs presented here, you need to download the CVS tables, name them appropiately and put them in this directory with the rest of the files.


## Taxi GPS Coordinates

The first question to ask is whether the data is useful, for example in order to predict the time it takes to go from point A to point B in Manhattan. In other words, it is important to ask whether the data covers the GPS coordinates we are intersted in. I wrote a Python code which is [here](\Taxi_Map_NYC.py) in this repsoitory that reads the data and plots the GPS coordinates of the taxi pick-up and drop-off locations for a sub-sample of the data on top of [Google Maps](https://maps.google.ca/). The code uses [Pygmaps](https://code.google.com/p/pygmaps/), a Python wrapper for Google Maps JavaScript API V3. Pygmaps provides functions to generate HTML file which shows your GPS data on Google map. 

The outputs of the code are two html files called [pickup_map.html](http://htmlpreview.github.io/?https://github.com/fkamiab/data_incubator_project/blob/master/pickup_map.html) and [dropoff_map.html](http://htmlpreview.github.io/?https://github.com/fkamiab/data_incubator_project/blob/master/dropoff_map.html), which take time to load as each contain 10000 points plotted on top of Google maps. If you would like less points, you can change [the code](\Taxi_Map_NYC.py) based on the comments in it.

I have also made a [PNG file](https://raw.githubusercontent.com/fkamiab/data_incubator_project/master/GPS_MAP.png) of reduced size which can be downloaded faster. As can be seen, each pick-up and drop-off locations give a trajectory for which travel time is shown in data. Therefore, if one knows the trajectories each user take on a regular basis, they can be compared to the ones in the data (the extrapolated results in time) to give future time predictions for the time spent by the user in their vehicle.

## Histograms for One Sample Trajectory

Now, we ask, how this can help in inferring statistical information on the trajectories a user takes in their travel schedule. Each such trajectory can be respresented as two GPS pairs, one for the starting point (e.g. the residence of the user) and the other pair for the desitination (e.g. the work place). I wrote [a code](https://github.com/fkamiab/data_incubator_project/blob/master/Finding_Trajectories.py) that takes thes two data points, and finds all trajectories in the Taxi data whose start and end points are one block away from the start and end points of the input trajectory. This are all therefore similar trajectories to the one of the resident, and can be used for giving statistical information on the resident's travel time. This information is plotted as histograms. 

[One of these histograms](https://raw.githubusercontent.com/fkamiab/data_incubator_project/master/Histogram_Hour.png) shows the distribution of the Taxi trajectories similar to the user's based on the hour in the day. We clearly see that there are more trajectories in busy times of the day, such as 9AM or 6PM. [A more important histogram](https://raw.githubusercontent.com/fkamiab/data_incubator_project/master/Histogram_Dur.png) shows the distribution of travel time durations for Taxi trajectories similar to the one of the user. We see they peek at about 10 to 11 minutes which can be used as an average prediction for the time of travel of the user. Finally I plot a [histogram](https://raw.githubusercontent.com/fkamiab/data_incubator_project/master/Histogram_Day.png) for the distribution of trajectories based on the day of the month. This can also be useful as it shows fluctuations in number, which can be among other factors a sign of difference between weekends and weekdays. 






