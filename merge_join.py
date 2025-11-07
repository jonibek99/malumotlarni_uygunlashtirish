import pandas as pd
import numpy as np
import requests as rq
movies=pd.read_csv('movies.csv')
rating=pd.read_csv('rating.csv')
df = pd.merge(movies, rating, left_on='id', right_on='movie_id')
slicing=df[['vote_count','director','title','year',]]

mer=slicing.to_csv('rating_movie.csv')
# print(rating.describe().info())
# print(movies.info())
# print(mer)
print(pd.read_csv('rating_movie.csv'))