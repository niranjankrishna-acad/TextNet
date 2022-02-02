import pandas as pd 


df = pd.read_csv("news.csv")
unique_vals = df.CATEGORY.unique()

for unique_val in unique_vals:
    dfcur = df[df['CATEGORY'] == unique_val]
    dfcur = dfcur['TITLE']
    dfcur.to_csv("data/{}.csv".format(unique_val))