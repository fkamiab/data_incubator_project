import numpy as np
import pandas as pd
import matplotlib.pylab as pl

df_day=pd.read_table('./Travel_Duration_Day.out')
df_month=pd.read_table('./Travel_Duration_Month.out')
#print df_day.sort(columns='Hour in the Day')

pl.rcParams.update({'font.size':15})

pd.DataFrame.hist(df_day, column="Hour in the Day", bins=24)
pl.savefig('Histogram_Hour.pdf', bbox_inches='tight')
#pl.show()
pd.DataFrame.hist(df_day, column="Duration Time (min)", bins=12)
pl.savefig('Histogram_Dur.pdf', bbox_inches='tight')

#pl.show()

pd.DataFrame.hist(df_month, column="Day of the Month", bins=31)
pl.savefig('Histogram_Day.pdf', bbox_inches='tight')

#pl.show()

#pl.plot(df_day['# hour'], df_day['dur_time'])
#pl.show()
