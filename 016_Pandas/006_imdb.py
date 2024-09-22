import pandas as pd


df = pd.read_csv("DataSets/imdb.csv")

result = df
result = df.columns
result = df.info
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df["Movie_Title"]
result = df["Movie_Title"].head()
result = df[["Movie_Title", "Rating"]].head()
result = df[["Movie_Title", "Rating"]].tail(7)
result = df[5:][["Movie_Title", "Rating"]].head() # ikinci 5 kaydı
result = df[5:10][["Movie_Title", "Rating"]] # ikinci 5 kaydı
result = df[df["Rating"] == 8][["Movie_Title", "Rating"]].head(10)
result = df[["Movie_Title", "YR_Released"]]
result = df[(df["YR_Released"] <= 2015) & (df["YR_Released"] >= 2014)][["Movie_Title", "YR_Released"]]


result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title", "Num_Reviews", "Rating"]]
# result = df.query("Num_Reviews >= 100000 | (Rating > 8.0 & Rating < 9.0)")[["Movie_Title", "Num_Reviews", "Rating"]]


print(result)
# print(len(result))




