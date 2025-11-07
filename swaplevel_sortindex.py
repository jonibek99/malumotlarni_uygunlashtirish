import pandas as pd
import numpy as np
import requests as rq

df1 = pd.read_csv('c.csv')

# Faqat kerakli ustunlar + indeksni o‘rnatish
df1 = df1.set_index(['Country', 'City'])
df1 = df1.loc[:, ['Air Quality', 'Water Pollution']]

df2 = pd.DataFrame()
df2['Water_quality'] = 100 - df1['Water Pollution']
df2['Air_polution'] = 100 - df1['Air Quality']

df3 = pd.DataFrame(
    df2.values,
    index=df1.index,   # 🔹 Bu yerda MultiIndex
    columns=[
        ['AIR', 'WATER'],
        ['Air_polution', 'Water_quality']
    ]
)

# Endi swaplevel ishlaydi ✅
swaplevel = df3.swaplevel('Country', 'City')
index=df3.sort_index(level=0, ascending=False)
print(index)
# print(swaplevel)
