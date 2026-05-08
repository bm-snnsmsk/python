def kontrol(deger) : return deger % 2 == 0

liste = [1, 10, 3, 5, 22, 12, 9]

print(list(map(kontrol, liste)))  # true false olarak döner
print(list(filter(kontrol, liste)))  # şartı sağlayan olanlar döner


print("".center(50,"*"))
print(liste)
check = lambda sayi : sayi % 2 == 0
print(list(map(check, liste)))
print(list(filter(check, liste)))

###################################333
isimler = ["ali","berfin","dilek","baran","tuba"]
filtre = list(filter(lambda i : i[0] == 'b', isimler))  ## 
print(filtre)  
sonuc = list(map(lambda i : i.upper(), filtre))  ## 
print(sonuc)  

###################################333
users = [
    {"ad":"ali","soyad":"sönmez"},
    {"ad":"ahmet","soyad":"kartal"},
    {"ad":"dilek","soyad":"güneş"}
]
filtre = list(filter(lambda i : len(i["soyad"]) > 5, users))  ## 
print(filtre)  
sonuc = list(map(lambda i : i["ad"], filtre))  ## 
print(sonuc)  

###### daha kısa gösterim
sonuc = [i["ad"] for i in users if len(i["soyad"]) > 5]
print(sonuc)
