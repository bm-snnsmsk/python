import pandas as pd
import numpy as np




data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["col1","col2","col3","col4","col5"])


result = df   ## df
result = df.columns # colon isimleri
result = df.head() # ilk 5 kayıt
result = df.head(5) # ilk 5 kayıt
result = df.head(10) # ilk 10 kayıt
result = df.tail() # son 5 kayıt
result = df.tail(5) # son 5 kayıt
result = df.tail(10) # son 10 kayıt
result = df["col2"].head(10) # col2'nin ilk 10 kaydı
result = df.col2.head(10) # col2'nin ilk 10 kaydı
result = df[["col2","col3"]].head() # col2 ve col3'nin ilk 5 kaydı
result = df[5:15][["col2","col3"]].head() # df'nin 5-15 aralığındaki col2 ve col3'nin ilk 5 kaydı

result = df > 50      ## tüm df True-False
result = df[df > 50]      ## tüm df True değerler diğerleri NaN
result = df[df % 2 == 0]      ## tüm df True değerler diğerleri NaN
result = df[df["col2"] % 2 == 0]      ## tüm df ama col2'si True olan satrırları 
result = df["col2"][df["col2"] % 2 == 0]      ## sadece col2 de col2'si True olan değerleri 
result = df[df["col2"] > 50 ][["col2","col3"]]      ## tüm df'de col2'si true olan satırların col2 ve col3 değerleri 
result = df[(df["col1"] > 50) & (df["col1"] <= 70)]      ## ve tüm df'de tüm kolonlar
result = df[(df["col1"] > 50) | (df["col1"] <= 70) | (df["col3"] <= 70)]      ## veya tüm df'de tüm kolonlar
result = df.query("(col2 >= 50 | col3 < 30 ) & col1 % 2 == 0")

print(result)