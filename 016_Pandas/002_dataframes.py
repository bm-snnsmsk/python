import pandas as pd

# series + series = dataframe

'''  
series       series           dataframe

apples      oranges          apples oranges
0 3          0 0            0  3   0
1 10    +    1 12      =    1  10  12
2 15         2 33           2  15  33
3 35         3 11           3  35  11

'''

# s1 = pd.Series(data=[3,10,15,35])
# s2 = pd.Series([0,12,33,11])
# data = dict(apples = s1, oranges = s2)  ## sutun adı = satır verisi
# df = pd.DataFrame(data)


df = pd.DataFrame()  ## boş df
df = pd.DataFrame([1,2,3,4])  ## tek sutunluk  4 satırlık df
df = pd.DataFrame([[1,2,3,4], [3,6,4,5], [7,8,9,10]])  ## 3 satırlık 4 sutunluk df
df = pd.DataFrame([["ahmet",50], ["ali",50], ["yağmur",50], ["çınar",50]])  ## 2 sutunluk 4 satırlık df

liste = ["ahmet",50], ["ali",50], ["yağmur",50], ["çınar",50]
df = pd.DataFrame(liste, columns=["name","derece"])  ## 2 sutunluk 4 satırlık df
df = pd.DataFrame(liste, columns=["name","derece"], index=[5,6,7,8])  ## 2 sutunluk 4 satırlık df

dict = {"isim":["ahmet","ali", "yağmur", "çınar"], "not":[50,60,70,80]}
df = pd.DataFrame(dict)  ## kolon bilgisine artık grek kalmaz
df = pd.DataFrame(dict, index=[212,333,444,555])  ## kolon bilgisine artık grek kalmaz

dic_list = [{"isim":"sinan", "derece":20},{"isim":"baran", "derece":70},{"isim":"zeynep", "derece":80},{"isim":"emine", "derece":88}]
df = pd.DataFrame(dic_list)
df = pd.DataFrame(dic_list, index=[212,333,444,555])









print(df)
