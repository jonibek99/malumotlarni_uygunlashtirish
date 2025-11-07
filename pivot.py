import pandas as pd

df = pd.read_csv('pivot.csv')

pivot = df.pivot_table(index='country', columns='bank_name', values='balance')
print(pivot)
