#Code written by Farbod Kamiab 
#The code reads GPS data from the New York City Taxi & Limousine Commission (NYCT&L) data on taxi trips and plots the GPS points on a map of New York City.

import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import pygmaps #One needs to install pygmaps to run this code

number_rows=14863778 #This is the total number of rows in the file  


# READING DATA
#Location of the file should be changed accordingly as the data file is too large to be uploaded on the Github repository  
df=pd.read_csv('./trip_data_1_2010.csv', nrows=number_rows, usecols=[' pickup_longitude', ' pickup_latitude', ' dropoff_longitude', ' dropoff_latitude']) 
#########################################################################


# SETTING COORDINATES OF THE MAP TO NEW YORK CITY
pickup_map = pygmaps.maps(40.752928, -73.881528, 12)
dropoff_map = pygmaps.maps(40.752928, -73.881528, 12)


# PUTTING POINTS ON THE MAP AND GETTING RID OF BAD DATA ROWS
for i in rows:
    pickup_lat=df[' pickup_latitude'][i]

    pickup_long=df[' pickup_longitude'][i]
    dropoff_lat=df[' dropoff_latitude'][i]
    dropoff_long=df[' dropoff_longitude'][i]

    if (isinstance(pickup_lat, float) and isinstance(pickup_long, float) and isinstance(dropoff_lat, float) and isinstance(dropoff_long, float)):
        
        pickup_map.addpoint(df[' pickup_latitude'][i], df[' pickup_longitude'][i], "#FF0000")
        dropoff_map.addpoint(df[' dropoff_latitude'][i], df[' dropoff_longitude'][i], "#0000FF")


# PRINTING OUTPUT
pickup_map.draw('./pickup_map.html')
dropoff_map.draw('./dropoff_map.html')
