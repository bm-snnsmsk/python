def kareal(sayi) : return sayi ** 2   ## ## lambda sayi: sayi**2    = kareal = lambda sayi: sayi**2   >>> ilgili fonyonu tek satırda göstermek gerekitrse

print(kareal(5))


kupAl = lambda i : i**3
kupAl(10)
sonuc = (lambda i : i**3)(10)
print(sonuc)


sayilar = [1,2,3,4,5]

########## map ###################
sonuc = list(map(kareal, sayilar))
print(sonuc)


########## map alternatif ################
for i in map(kareal, sayilar):
    print(i)

########## map alternatif lambda (genelde tek satırlık ve bir iki defa kullanılacak fonksiyonlar için alternatiftir) ################
sonuc = list(map(lambda x: x ** 3, sayilar))
print(sonuc)

liste = [3, 5, 4, 8, 7, 15, 14]
f = lambda i :  i % 2 
print(list(map(f, liste)))

########## lambda ################
elveda = lambda : print("Güle güle")
elveda()

###################################333
sayilar222 = ["1","2","3","4","5"]
sonuc = list(map(int, sayilar222))  ## int strleri integere cevirir
print(sonuc)   

###################################333
isimler = ["ali","berfin","dilek","baran","tuba"]
sonuc = list(map(str.capitalize, isimler))  ## 
print(sonuc)   

###################################333
users = [
    {"ad":"ali","soyad":"sönmez"},
    {"ad":"ahmet","soyad":"kartal"},
    {"ad":"dilek","soyad":"güneş"}
]
sonuc = list(map(lambda i : i["ad"], users))  ## 
print(sonuc) 
