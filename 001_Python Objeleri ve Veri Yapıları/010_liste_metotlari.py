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

numbers.insert(3, 78)   # araya eleman ekleme
numbers.insert(-1, 99)
print(numbers[3])

print(numbers)
numbers.pop() # son eleman  '3'
numbers.pop(1) # 10
numbers.pop(-1) # son eleman  99
numbers.pop(7)   # 7
print(numbers)

numbers.remove(40)    ## verilen değeri sil  değer yok ise hata verir


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

print(letters.index("g"))  ## 5. index

letters.pop(letters.index("b"))
print(letters)
numbers.clear()   ## tüm dizi elemanları siler

varmi1 = "y" in letters
varmi2 = letters.index("y")

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
