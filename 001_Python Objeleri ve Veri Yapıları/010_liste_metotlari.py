numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a","g","s","b","y","a","s"]

print(min(numbers))
print(min(letters))

print(max(numbers))
print(max(letters))

print(numbers[3:6])

numbers[4] = 40   ## değer güncelleme
print(numbers[4])

numbers.append(49)
numbers.append("3")
print(numbers)

#############
liste = ["sinan", 23, "s", 22, 10, "baran"]
print(liste)
liste.append(10)   ### sona eleman ekler
liste.append(10)
liste.append(10)
print(liste)
#############

numbers.insert(0, 100)   # başa eleman ekleme
numbers.insert(3, 78)   # araya eleman ekleme
numbers.insert(-1, 99)   ### sondan bir önceye 99 ekle
numbers.insert(len(liste), "baran")  ## en sona ekler
print(numbers[3])

print(numbers)
numbers.pop() # son eleman  '3'
numbers.pop(0) # ilk elemanı sil
numbers.pop(-1) # son elemanı sil  99
numbers.pop(7)   # 7. elemaı sil
print(numbers)

numbers.remove(40)    ## verilen değeri sil  değer yok ise hata verir, değerde birden fazla varsa her defsında bir tane siler (ilk bulduğu elemnı siler)


numbers.sort()    ## sıralar küçükten büyüğe
letters.reverse() ## mevcut diziyi tersine çevirir

print(numbers)
print(letters)

kac_tane = numbers.count(10)  # 1
kac_tane2 = numbers.count("s") # 0
kac_tane3 = letters.count("s")  #2
print(kac_tane)
print(kac_tane2)
print(kac_tane3)

print(letters.index("g"))  ## 5. index  birden fazla varsa ilk elennın indexini döndürür

letters.pop(letters.index("b"))
print(letters)
numbers.clear()   ## tüm dizi elemanları siler

varmi1 = "y" in letters
varmi2 = letters.index("y")

print("baran" in liste)

print(varmi1)  # True
print(varmi2)  ## 2

letters2 = ["sinan","baran","emine","tuba nur","kendal","ibrahim"]
print(letters2)
letters2.reverse() # ters çevirir
letters2[::-1] # ters çevirir
print(letters2)

letters2.sort()  ## sırala
letters2.reverse() # z-a
print(letters2)

letters.clear()    ## dizi içeriğini boşaltır

#################################################
# STACK (last in first out)
liste = []
liste.append(10) ## 
liste.append(30) ## 
liste.append(50) ## 
liste.pop()


##################################################

# QUEUE (first in first out)
liste2 = []
liste2.append(10) ## 
liste2.append(30) ## 
liste2.append(50) ## 
liste2.pop(0)

##################################################

diğer mtodlar 
https://www.w3schools.com/python/python_lists_methods.asp



