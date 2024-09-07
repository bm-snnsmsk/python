sayi = int(input("bir sayı gir  : "))

asalMi = True

if sayi == 1 or sayi == 0 or sayi < 0 :
    asalMi = False
else :
    for i in range(2, sayi) :
        if sayi % i == 0 :
            asalMi = False
            break

if asalMi :
    print(f"{sayi}, asal sayıdır")
else :
    print(f"{sayi}, asal sayı değildir")






  





