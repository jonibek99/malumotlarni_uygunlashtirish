import pandas as pd
import numpy as np
import requests as rq
data=pd.Series(np.random.rand(9),index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,2,3,4,5,6]])
print(data.unstack().stack())