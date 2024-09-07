# fonksiyon
# metot = class fonksiyonlari

def selam(name = "user") :
    print("selam " + name)

selam("sinan")
selam("baran")
selam()


def selam2(name = "user22") :
    return "selam " + name

print(selam2())

def toplam(num1, num2) :
    return num1 + num2

print(toplam(20,30))


########################################################################
def yasHesapla(dogumYili) :
    return 2024 - dogumYili

def emekliligeKacYilKaldi(dogumYili, name) :
    ''' 
    emelilik yası hesaplama 
    DOCSTRING : dogum yilina gore emeklilik
    INPUT : dogum yili
    output:hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    
    if emeklilik > 0 :
        print(f"sayin {name}, emeliliğinize {emeklilik} yıl kaldı.")


emekliligeKacYilKaldi(1985, "Sinan")

liste = [1,2,3]
help(help(liste.append))
help(emekliligeKacYilKaldi)