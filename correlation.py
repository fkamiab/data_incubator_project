#Code written by Farbod Kamiab
#The code plots distance versus travel time for 10000 points in the data 

import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import statsmodels.api as sm
import plot_fit as pfit
import pygmaps

number_rows=10000
df=pd.read_csv('~/Downloads/data/trip_data_1_2010.csv', nrows=number_rows)


df_time_distance= df[[' trip_time_in_secs', ' trip_distance']]
time_sorted_df_time_distance= df_time_distance.sort_values(' trip_time_in_secs')
nbegin=int(number_rows/5.3)
time=time_sorted_df_time_distance[' trip_time_in_secs'][nbegin:]
distance= time_sorted_df_time_distance[' trip_distance'][nbegin:]
result = sm.OLS( distance, time ).fit()
fig, ax = pl.subplots()
fig = pfit.plot_fit(result, 0, ax=ax)
ax.set_ylabel("Distance (miles)")
ax.set_xlabel("Time (min)")
pl.savefig('Correlation.png', bbox_inches='tight')



