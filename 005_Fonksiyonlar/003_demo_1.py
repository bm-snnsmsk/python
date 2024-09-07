def asalSayilar(sayi1, sayi2) :
    kucuk = 0
    buyuk = 0
    asal_sayilar = []
    if sayi1 > 0 and sayi2 > 0 :
        if sayi1 > sayi2 :
            buyuk = sayi1
            kucuk = sayi2
            print("sayi1 > sayi2 bloğu çalıştı")
        elif sayi2 > sayi1 :
            buyuk = sayi2
            kucuk = sayi1
            print("sayi1 < sayi2 bloğu çalıştı")
        elif sayi1 == sayi2 :
            print("sayılar eşit olmaz. Farklı değerler girin")
        else : 
            print("else bloğu çalıştı")  
                   
    else : 
        print("sayılar negatif olamaz. lütfen posiztif sayılar girin")
    ####################################################################3
    for i in range(kucuk, buyuk + 1):
        isAsal = True
        for j in range(2, i):
            if i % j == 0 :
                # print(f"{i} {j}'yi tam bölüyor. Bu yüzden {i} sayısı asal değildir")
                isAsal = False
                break
        if isAsal :
            asal_sayilar.append(i)
    # return asal_sayilar
    print(asal_sayilar)

    

# print(asalSayilar(7,17))
asalSayilar(13,91)



