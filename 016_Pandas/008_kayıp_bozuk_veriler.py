import pandas as pd
import numpy as np


## NaN
data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1", axis = 1)  ## sutun sil
result = df.drop(["column1","column2"], axis = 1) ## suunları sil
result = df.drop('a', axis = 0)   ## satırı sil
result = df.drop(['a','b','h'], axis = 0) ## satırları sil


result = df.isnull()  ## NaN True var olan değerler False
result = df.notnull()  ## NaN False var olan değerler True
result = df.isnull().sum()  ## her sutunun NaN sayıları
result = df["column1"].isnull().sum() ## column1 sutunun NaN sayıları
result = df[df["column1"].isnull()]  ## column1 değeri NaN olan satırlar
result = df[df["column1"].isnull()]["column1"] ## column1 değeri NaN column1 sutunu
result = df[df["column1"].notnull()]["column1"]


result = df.dropna() # axis = 0 => satıra  ## içinde NaN olan satırları sil
result = df.dropna(axis = 1) # axis = 1 => ## içinde NaN olan sutunları sil
result = df.dropna(how = "any") # axis = 0 => satıra  ## içinde bir tane NaN bile olsa satırları sil
result = df.dropna(how = "all") # axis = 0 => satıra  ## hepsi NaN olan satırları sil
result = df.dropna(subset  = ["column1","column2"], how = "all") ## sadece belirlenen kolunlarda hepsi NaN olan satırları sil
result = df.dropna(subset  = ["column1","column2"], how = "any") ## sadece belirlenen kolunlarda bir tane bile NaN olsa satırları sil
result = df.dropna(thresh = 2) # en az sayıda normal veri
result = df.dropna(thresh = 3) # en az sayıda normal veri


result = df.fillna(value = 'no input') ## NaN değerleri belirlenen değerle doldur
result = df.fillna(value = 1) ## NaN değerleri belirlenen değerle doldur

result = df.sum() ## her kolonun toplamı
result = df.sum().sum()   ## tüm kolonların toplamı
result = df.size  ## tüm verilerin adedi
result = df.isnull().sum() ## NaN değerlerin sayıları
result = df.isnull().sum().sum() ## tüm df'de toplam NaN adedi


#### fonksiyon start (NaN değerlerin yerine ortalama yazdır) ####
def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))
#### fonksiyon end ####


print(df)
print("###################################################")
print(result)