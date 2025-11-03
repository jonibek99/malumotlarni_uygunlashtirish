import pandas as pd
import numpy as np
df=pd.read_csv('c.csv')
# pivot_table = pd.pivot_table(df,index=['City','Country'])
# c=df.loc[['Russia']]
print(df[df['Country']=='Uzbekistan'])
