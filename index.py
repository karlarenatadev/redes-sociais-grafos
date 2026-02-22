import pandas as pd

df = pd.read_csv('instagram.csv')

print(df.info())
print(df["media_type"].unique())