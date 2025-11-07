import pandas as pd
import numpy as np
import requests as rq

df=pd.read_csv('bank.csv')
bank1,bank2,bank3,bank4=df[:25],df[25:50],df[50:75],df[75:]
concat=pd.concat([bank1,bank2,bank3],axis=1)
print(concat)