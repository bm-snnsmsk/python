def kareal(sayi) : return sayi ** 2

print(kareal(5))

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