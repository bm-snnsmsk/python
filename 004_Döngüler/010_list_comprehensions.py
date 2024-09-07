sayilar = []
for i in range(10) :
    sayilar.append(i)
print(sayilar)
######################################################
numbers = [x for x in range(10)]
print(numbers)
######################################################
numbers2 = [x*x for x in range(10)]
print(numbers2)
######################################################
numbers3 = [x*x for x in range(10) if x %3 == 0]
print(numbers3)
######################################################
listem = [i for i in "Sinan Şimşek" ]
print(listem)
######################################################
yillar = [1983, 1999, 2008, 1956, 1986]
yaslar = [2024 - i for i in yillar ]
print(yaslar)
######################################################
sonuc = [i if i % 2 == 0 else "Tek" for i in range(1,10) ]
print(sonuc)
############  iç içe for ########################
sonuc1 = [(i,j) for i in range(3) for j in range(3) ]
print(sonuc1)
######################################################
