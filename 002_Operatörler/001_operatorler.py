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
print(x,y,z)   ### 1 2 [3, 4, 5]

x, *y, z = values  
print(x,y,z)   ### 1 [2, 3, 4] 5


print(3**4)
print(30%7)
print(30//7)

print("Karşılaştırma Operatörleri".center(50,"*"))

print(30 == 7)  ## False
print(30 > 7)   ## True
print(30 >= 7)   ## True
print(30 < 7)   ## False
print(30 <= 7)  ## False
print(30 != 7)   ## True
print(30 % 2 == 0)  ## True
print(29 % 2 == 0)  ## False

print("Mantıksal Operatörler".center(50,"*"))

print(30 == 7 and 30 > 7) ## (True ve True = True) False
print(30 == 7 or 30 > 7) ## (True veya True = True) True
print(not(30 == 7 and 30 > 7)) ## True
print(not 30 == 7 or 30 > 7)  ## True
print(not(30 == 7 or 30 > 7))  ## False
print(not 30 == 7) ## True   = print(30 != 7) ## True

### uygulama 1 >> girilen iki sayıdan hangisi büyük
sayi1 = input("Birinci sayıyı giriniz : ")
sayi2 = input("İkinci sayıyı giriniz : ")

if int(sayi1) > int(sayi2) :
    print(f"{sayi1} sayısı {sayi2}'den büyüktür.")
elif int(sayi1) < int(sayi2) :
    print(f"{sayi1} sayısı {sayi2}'den küçüktür.")
elif int(sayi1) == int(sayi2) :
    print(f"{sayi1} sayısı {sayi2}'a eşittir.")
  
### uygulama 2 >> vize (30%) ve final (%70)  = 50 den büyükse geçti 
vize = input("Vize giriniz : ")
final = input("final giriniz : ")
sonuc = int(vize)*0.3 + int(final)*0.7
if sonuc > 50 :
    print(f"Sonuç : {str(sonuc)}, Başarılı")
else :
    print(f"Sonuç : {str(sonuc)}, Başarısız")
  
### uygulama 3 >> girilen sayı çift mi tek mi
sayi = input("Sayı giriniz : ")
sonuc = int(sayi) % 2 
if sonuc == 0 :
    print(f"Sonuç : {str(sonuc)}, Sayı çift")
else :
    print(f"Sonuç : {str(sonuc)}, Sayı tek")
  
### uygulama 4 >> girilen sayı negatif mi pozitif mi
sayi = input("Sayı giriniz : ")
sonuc = int(sayi) 
if sonuc >= 0 :
    print(f"Sonuç : {str(sonuc)}, Sayı pozitif")
else :
    print(f"Sonuç : {str(sonuc)}, Sayı negatif")
  
### uygulama 5 >> girilen username ve şifre sorgula
username = input("username giriniz : ")
password = input("şifre giriniz : ")
if username.strip().lower() == "sinan" and password.strip().lower() == "1234" :
    print(f"Giriş başarılı. Hoşgeldiniz, {username.title()}")
else :
    print(f"Giriş başarısız")

### uygulama 6 >> girilen sayı 0-100 aralığında mı
sayi = input("Bir sayı giriniz : ")

if int(sayi) > 0 and  int(sayi) < 100 :
    print(f"{sayi} 0-100 aralığındadır.")
else :
    print(f"{sayi} 0-100 aralığında değildir.")
############################################################


print("Identity ve Membership Operatörleri".center(50,"*"))
liste1 = liste2 = [1,2,3]
liste3 = [1,2,3]

print(liste1 == liste2)  ### True  
print(liste1 == liste3)  ### True

### referasları aynı mı
print(liste1 is liste2)     # True   ## is demek aynı adresi tutup tutmadığı yani tamamen aynılar mı
print(liste1 is liste3)     # False
print(liste1 is not liste3)     # True

liste4 = ["apple", "banana"]
print("cherry" in liste4)      # false   # listede ilgili eleman var mı
print("apple" in liste4)       # true
print("apple" not in liste4)   # false
