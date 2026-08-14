sayi = int(input("bir sayı gir  : "))

asalMi = True

if sayi == 1 or sayi == 0 or sayi < 0 :
    asalMi = False
elif sayi == 2 :
    asalMi == True
else :
    for i in range(2, sayi + 1) :
        if sayi % i == 0 :
            asalMi = False
            break

if asalMi :
    print(f"{sayi}, asal sayıdır")
else :
    print(f"{sayi}, asal sayı değildir")







  





