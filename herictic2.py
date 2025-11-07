import pandas as pd
import numpy as np
import requests as rq

df1 = pd.read_csv('c.csv')
df1 = df1.loc[:, ['Air Quality', 'Water Pollution']]

df2 = pd.DataFrame()
df2['Water_quality'] = 100 - df1['Water Pollution']
df2['Air_polution'] = 100 - df1['Air Quality']

df3 = pd.DataFrame(
    df2.values,
    index=df2.index,
    columns=[
        ['AIR', 'WATER'],
        ['Air_polution', 'Water_quality']
    ]
)

print(df3['AIR'])
