sayi1 = int(input("bir sayı gir : "))
sayi2 = int(input("bir sayı gir : "))

buyuk = 0
kucuk = 0

if sayi1 > sayi2 :
    buyuk = sayi1
    kucuk = sayi2
else :
    buyuk = sayi2
    kucuk = sayi1


while kucuk <= buyuk :
    if kucuk % 2 == 1 :
        print(kucuk)
    kucuk += 1

print("2. örnek".center(50,"*"))
i = 100
while i > 0 :
    print(i)
    i -= 1


