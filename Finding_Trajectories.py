#Code written by Farbod Kamiab.
#The code takes the GPS location of a city resident and one of their destinations (in other words a trajectory), and finds all trajectories in the data whose start and end points are one block away from the start and end points of the input trajectory. This are all therefore similar trajectories to the one of the resident, and can be used for giving statistical information on the resident's travel time. This information is plotted as histograms.

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl


#TAKES STARTING LOCATION OF THE USER, FOR EXAMPLE THEIR RESIDENTIAL GPS LOCATION
begin_GPS_long=-73.998516
begin_GPS_lat= 40.740020

#TAKES ONE DESTINATION LOCATION
end_GPS_long=-73.993688
end_GPS_lat= 40.767011

#ONE BLOCK SIZE IN MANHATTAN IN TERMS OF DEGREES
block_size=0.001867

#READING THE DATA FILE (EACH FILE IS ABOUT 2 GB)
df=pd.read_csv('./trip_data_1_2010.csv')

#SELECTS TAXI TRAJECTORIES IN THE DATA THAT ARE ONE BLOCK CLOSE TO THE TRAJECTORY OF THE USER
df_selected= df[(df[' pickup_longitude']<begin_GPS_long + block_size) 
& (df[' pickup_longitude']> begin_GPS_long - block_size) 
& (df[' pickup_latitude']<begin_GPS_lat + block_size) 
& (df[' pickup_latitude']>begin_GPS_lat - block_size) 
& (df[' dropoff_longitude']<end_GPS_long + block_size) 
& (df[' dropoff_longitude']>end_GPS_long - block_size) 
& (df[' dropoff_latitude']<end_GPS_lat + block_size) 
& (df[' dropoff_latitude']>end_GPS_lat - block_size)]

#EXTRACTS DATE AND TIME INFORMATION ON THOSE TRAJECTORIES
hour = np.zeros(len(df_selected))
minute = np.zeros(len(df_selected))
day = np.zeros(len(df_selected))
dur_time=np.zeros_like(hour)
new_df=df_selected.reset_index()
for i in range(0, len(df_selected)):
    timestamp= pd.Timestamp(new_df[' pickup_datetime'][i])
    hour[i]=timestamp.hour
    minute[i]=timestamp.minute
    day[i]=timestamp.day
    dur_time[i]=new_df[' trip_time_in_secs'][i]


#SAVES THE INFORMATION
np.savetxt('Travel_Duration_Month.out', np.c_[day, dur_time], delimiter='\t', header='day\tdur_time')
np.savetxt('Travel_Duration_Day.out', np.c_[hour+minute/60., dur_time], delimiter='\t' , header='hour\tdur_time') 


#READS THE INFO (ORIGINALLY DONE IN A SEPARATE MODULE)
df_day=pd.read_table('./Travel_Duration_Day.out')
df_month=pd.read_table('./Travel_Duration_Month.out')


#PLOTS HISTOGRAMS FOR THE DISTRIBUTION OF THE HOUR OF THE DAY, THE DURATION TIME AND THE DAY OF THE MONTH OF THE TRAJECTORIES
pl.rcParams.update({'font.size':15})
pd.DataFrame.hist(df_day, column="Hour in the Day", bins=24)
pl.savefig('Histogram_Hour.png', bbox_inches='tight')
pd.DataFrame.hist(df_day, column="Duration Time (min)", bins=12)
pl.savefig('Histogram_Dur.png', bbox_inches='tight')
pd.DataFrame.hist(df_month, column="Day of the Month", bins=31)
pl.savefig('Histogram_Day.png', bbox_inches='tight')
