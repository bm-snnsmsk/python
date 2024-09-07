import random

hak = 5
puan = 0
sayac = 0

sayi = random.randint(1,101)
while hak > 0 :
    hak -= 1
    sayac += 1    
    puan = 100 - ((sayac - 1) * 20)

    tahmin = int(input("1-100 arasında bir sayı gir sayı  : "))
    if hak == 0 :
        print(f"malesef hakkınız kalmadı {sayi} -- puanınız : {puan}")
        break

    if sayi == tahmin :
        print(f"Tebrikler, {sayac}. defada bildiniz.. kalan hakkınız : {hak} --  sayı : {sayi} -- puanınız : {puan}")
        break
    elif sayi > tahmin :
        print(f"daha büyük bir sayı deneyin, kalan hakkınız : {hak} --  sayı : {sayi}")
    else :
        print(f"daha küçük bir sayı deneyin, kalan hakkınız : {hak} --  sayı : {sayi}")






