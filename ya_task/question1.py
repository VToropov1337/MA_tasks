import pandas as pd
import numpy as np
import matplotlib




df = pd.read_csv('NASA_access_log_Jul95.txt',sep=' ',\
encoding='ISO-8859-1',header=None,\
error_bad_lines=False,engine='c',\
infer_datetime_format=True)


df.head()
df = df[df[4].notnull()]
df[5].value_counts(ascending=False).head(15) #самые популярные топ15
