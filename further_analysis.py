import numpy as np
import pandas as pd
import matplotlib.pyplot as pl


begin_GPS_long=-73.998516
begin_GPS_lat= 40.740020

end_GPS_long=-73.993688
end_GPS_lat= 40.767011

block_size=0.001867 *3.



number_rows=100000

df=pd.read_csv('~/Downloads/data/trip_data_1_2010.csv', nrows=number_rows)
rows = np.random.choice(df.index.values, 10000)
sampled_df = df.ix[rows]

df_selected= sampled_df[(df[' pickup_longitude']<begin_GPS_long + block_size) 
& (df[' pickup_longitude']> begin_GPS_long - block_size) 
& (df[' pickup_latitude']<begin_GPS_lat + block_size) 
& (df[' pickup_latitude']>begin_GPS_lat - block_size) 
& (df[' dropoff_longitude']<end_GPS_long + block_size) 
& (df[' dropoff_longitude']>end_GPS_long - block_size) 
& (df[' dropoff_latitude']<end_GPS_lat + block_size) 
& (df[' dropoff_latitude']>end_GPS_lat - block_size)]

hour = np.zeros(len(df_selected))
minute = np.zeros(len(df_selected))
dur_time=np.zeros_like(hour)
new_df=df_selected.reset_index()
for i in range(0, len(df_selected)):
    timestamp= pd.Timestamp(new_df[' pickup_datetime'][i])
    hour[i]=timestamp.hour
    minute[i]=timestamp.minute
    dur_time[i]=new_df[' trip_time_in_secs'][i]





pl.rcParams.update({'font.size':15})



pl.plot(hour+minute/60., dur_time, 'bo')
pl.xlabel('Hour in the Day', fontsize=20)
pl.ylabel('Travel Duration (min)', fontsize=20)
pl.savefig('Travel_Duration.pdf', bbox_inches='tight')
#pl.show() 



