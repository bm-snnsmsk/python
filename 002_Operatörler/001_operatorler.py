print("Atama Operatörleri".center(50,"*"))

# x = 20
# y = 30 
# z = 40

x,y,z = 20,30,40
print(x,y,z)

x,y = y,x
print(x,y,z)

x += 5       #  x = x + 5  
x -= 5       #  x = x - 5  
x *= 5       #  x = x * 5  
x /= 5       #  x = x / 5  
x %= 5       #  x = x % 5 
y //= 5      #  y = y // 5   ## tam bölme
y **= 5      #  y = y ** 5   ## üs alma

print(x,y,z)

values = 1, 2, 3, 4, 5
x, y, *z = values     # sağdaki her eleman soldaki bir elemanla eşleşir fazla olan değerler * işareti ile istenen değere liste olarak atanabilir

print(x,y,z)

print(3**4)
print(30%7)
print(30//7)

print("Karşılaştırma Operatörleri".center(50,"*"))

print(30 == 7)
print(30 > 7)
print(30 >= 7)
print(30 < 7)
print(30 <= 7)
print(30 != 7)
print(30 % 2 == 0)
print(29 % 2 == 0)

print("Mantıksal Operatörler".center(50,"*"))

print(30 == 7 and 30 > 7)
print(30 == 7 or 30 > 7)
print(not(30 == 7 and 30 > 7))
print(not 30 == 7 or 30 > 7)
print(not(30 == 7 or 30 > 7))
print(not 30 == 7)


print("Identity ve Membership Operatörleri".center(50,"*"))
liste1 = liste2 = [1,2,3]
liste3 = [1,2,3]

print(liste1 == liste2)
print(liste1 == liste3)

print(liste1 is liste2)     # false   ## is demek aynı adresi tutup tutmadığı yaniş tamamen aynılar mı
print(liste1 is liste3)     # true
print(liste1 is not liste3)     # false

liste4 = ["apple", "banana"]
print("cherry" in liste4)      # false   # listede ilgili eleman var mı
print("apple" in liste4)       # true
print("apple" not in liste4)   # false