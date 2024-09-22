import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3), index=["a","b","c"], columns=["col1","col2","col3"])
result = df["col2"]
# result = type(df["col2"])
result = df[["col1","col2"]]
result = df.loc["a"]  ## a satırı
result = type(df.loc["a"])

## loc["row", "column"]
# loc["row"]
# loc["column"]
# loc[:, "column"]   


result = df.loc[:, "col1"] # her satırın col1 değeri
result = df.loc[:, ["col1", "col2"]] # her satırın col1 ve col2 değeri
# result = df.loc[:, "col1": "col3"] # her satırın col1 ve col3 değer aralığı
result = df.loc[:, :"col2"] # her satırın baştan ve col2 değere kadar
# result = df.loc["a":"c", :"col2"] # a-c satırın baştan ve col2 değere kadar
result = df.iloc[0] # her satırın ilk kolonu
result = df.loc["b", "col2"] # kesişim değeri
result = df.loc[["a","b"], ["col1","col2"]] # kesişim değeri

df["col4"] = pd.Series(randn(3), ["a","b","c"])  ## sutun ekleme
df["col5"] = df["col3"] + df["col4"]  ## sutun ekleme

silinen_sutun = df.drop("col2", axis=1) ## sütun silme inplace=False
silinen_satir = df.drop("c", axis=0) ## satir silme inplace=False
silinen_satir = df.drop("c", axis=0, inplace=True) ## satir siler ve orginal df üzerinde güncelleme yapar


print(df)
print(result)
print(silinen_sutun)
print(silinen_satir)