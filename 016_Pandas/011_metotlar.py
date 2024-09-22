import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)



result = df
result = df["Column2"].unique()  ## benzersi olanları getir
result = df["Column2"].nunique()  ## benzersiz olanların sayıları
result = df["Column2"].value_counts()  ## her eleman kaç defa tekrar ediyor
result = df["Column1"] * 2  ## hr elemanı 2 ile çarp

# def kareal(x):
#     return x * x
# result = df["Column1"].apply(kareal)  ## fonksiyon ekleme

# kareal2 = lambda x: x * x
# result = df["Column1"].apply(kareal2)

# result = df["Column1"].apply(lambda x: x * x)

df["Column4"] = df["Column3"].apply(len) ## karakter sayılarını hesapla ve yeni bir kolona ata ve df yi güncelle
# print(df)

result = df.columns ## kolon isimler
# result = len(df.columns) ## kolon sayıları
result = df.index ## satır-index bilgileri
result = len(df.index) ## toplam satır-index
result = df.info

result = df.sort_values("Column2") ## colon2'e göre sırala (artan)
result = df.sort_values("Column3") 
result = df.sort_values("Column3", ascending = False) # ascending = False  =azalan

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df)
# print(result)
print(df.pivot_table(index="Ay",columns= "Kategori", values= "Gelir"))  ## 3 kolonluk df, index ay bilgisine göre, kolon kategori bilgisine göre, değerler ie gelire göre

'''
        Ay    Kategori  Gelir
0    Mayıs  Elektronik     20
1  Haziran  Elektronik     30
2    Nisan  Elektronik     15
3    Mayıs       Kitap     14
4  Haziran       Kitap     32
5    Nisan       Kitap     42
6    Mayıs       Giyim     12
7  Haziran       Giyim     36
8    Nisan       Giyim     52



Kategori  Elektronik  Giyim  Kitap
Ay
Haziran         30.0   36.0   32.0
Mayıs           20.0   12.0   14.0
Nisan           15.0   52.0   42.0

'''
