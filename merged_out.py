import pandas as pd
import numpy as np
import requests as rq


a=pd.DataFrame({'Noutbuk':['Hp','Mac','Asus'],
                'xotirasi':['2 tb','1 tb','250 gb']})
b=pd.DataFrame({'Noutbuk':['Hp','Mac','vivo book'],
                'narxi':['250 dollor','300','100']})
merge=pd.merge(a,b)
merge_left=pd.merge(a,b,how='left')
merge_right=pd.merge(a,b,how='right')
# merged_outer=pd.merge(a,b,how='outer')
# # print(merge)
# print(merged_outer.to_csv('noubooks.csv'))
# print(merge_left)
print(merge_right)