sayilar = [1, 53, 4, 5, 65, 23]

sayilar.sort()   ## listede güncelleme yapılmaz
sonuc = sorted(sayilar)   ## listede güncelleme yapar
sonuc = sorted(sayilar, reverse=True)   ## listede güncelleme yapar, azalan
print(sayilar)
print(sonuc)

############################ dictionary
sonuc2 = sorted(sayilar, key=len) ## key sayıları
sonuc2 = sorted(sayilar, key=lambda i : i ["username"]) ## isimlere göre 
