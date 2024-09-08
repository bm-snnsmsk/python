def ortalamalari_oku() :
    with open("Dosyalar/sinav_notlari.txt", "r", encoding="utf-8") as file :
        # sayac = 0 
        for i in file : 
            # print(i.strip())
            # sayac += 1
            print(not_hesapla(i))
        # print(sayac)

def harf_notu_hesapla(ortalama) :
    if ortalama >= 90 and  ortalama <= 100 :
        harf = "AA"
    elif ortalama >= 85 and  ortalama < 90 :
        harf = "BA"
    elif ortalama >= 80 and  ortalama < 85 :
        harf = "BB"
    elif ortalama >= 75 and  ortalama < 80 :
        harf = "CB"
    elif ortalama >= 70 and  ortalama < 75 :
        harf = "CC"
    elif ortalama >= 65 and  ortalama < 70 :
        harf = "DC"
    elif ortalama >= 60 and  ortalama < 65 :
        harf = "DD"
    elif ortalama < 50:
        harf = "FF"
    
    return harf
   

def not_hesapla(satir) :
    satir = satir[:-1]
    liste = satir.split(":")    
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1+not2+not3)/3
    # harf = harf_notu_hesapla(ortalama)
    # print(ogrenciAdi+ ":"+harf+"\n")
    return ogrenciAdi + ":" + str(ortalama) + '\n'

def not_gir() :
    ad = input("öğrenci adı :")
    soyad = input("öğrenci soyadı :")
    not1 = input("not 1 :")
    not2 = input("not 2 :")
    not3 = input("not 3 :")

    with open("Dosyalar/sinav_notlari.txt", "a", encoding="utf-8") as file :
        file.write(ad +" "+soyad+":"+not1+","+not2+","+not3+"\n")

def notlari_kaydet() :
    with open("Dosyalar/sinav_notlari.txt", "r", encoding="utf-8") as file :
        liste = []
        for i in file :
            liste.append(not_hesapla(i))

        with open("Dosyalar/sonuclar.txt", "w", encoding="utf-8") as file2 :
            for i in liste :
                file2.write(i)


while True :
    islem = input("1 - Notları oku\n2 - Not Gir\n3 - Notları Kaydet\n4 - Çıkış\nLütfen bir seçim yapın : ")

    if islem == "1" :
        ortalamalari_oku()
    elif islem == "2" :
        not_gir()
    elif islem == "3" :
        notlari_kaydet()
    else :
        break

