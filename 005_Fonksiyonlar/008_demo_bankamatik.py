hesapSinan = {
    "ad" :"Sinan Şimşek",
    "hesapNo" :"123456",
    "bakiye" :3000,  ## dictionary olduğu için günceleme yapılır
    "ekHesap" :2000,
} # referans değer değil de value değer olsaydı mevcut değerler üzerinde güncelleme yapılmazdı
hesapBaran = {
    "ad" :"Baran Şimşek",
    "hesapNo" :"164976",
    "bakiye" :13000,
    "ekHesap" :1000,
}
hesapTuba = {
    "ad" :"Tuba Şimşek",
    "hesapNo" :"547856",
    "bakiye" :30000,
    "ekHesap" :0,
}

def guncelBakiye(hesap, msj  = "") :
    print(f"Güncel Bakiyeniz : {hesap['bakiye']} -- Güncel EkHesap Bakiyeniz : {hesap['ekHesap']}. {msj}")

def para_yatir(hesap, miktar) :
    eksikEkHesap = 2000 - hesap['ekHesap']    
    if hesap['ekHesap'] < 2000 :
        hesap['ekHesap'] += eksikEkHesap
        hesap['bakiye'] =+ (miktar - eksikEkHesap)
        guncelBakiye(hesap, "Ek hesap borcunuz ödendi.")
    else :
        hesap['bakiye'] += miktar
        guncelBakiye(hesap, "Para yatırma işlemi başarılı")



def paracek(hesap, miktar) :
    print(f'Merhaba {hesap["ad"]}')
    if (hesap["bakiye"] >= miktar) :
        guncelBakiye(hesap, "Parayı çekebilirsiniz...")
        hesap["bakiye"] -= miktar
        guncelBakiye(hesap)
    elif (hesap["bakiye"] + hesap["ekHesap"] >= miktar) : 
        ekHesapKullanilsinmi = input("Ek hesap kullanılsın mı ? (e/h) : ") 
        if ekHesapKullanilsinmi.lower() == "e" :
            guncelBakiye(hesap, "Parayı çekebilirsiniz...")
            hesap["ekHesap"] = (hesap["ekHesap"] - (miktar - hesap["bakiye"]))
            hesap["bakiye"] = 0
            guncelBakiye(hesap)
        else:
            guncelBakiye(hesap, "Para çekmekten vazgeçtiniz. İyi günler dileriz.")
    else: 
        guncelBakiye(hesap, "Toplam bakiyeniz yeterli değil")



paracek(hesapSinan,4300)
para_yatir(hesapSinan, 4500)



"""
print("Banka uygulamasına hoş geldiniz...")   
banka = {
        'default' :{"bakiye":1000, 'ekhesap': 1000} ,
        'sinan' :{"bakiye":1000, 'ekhesap': 1000} ,
    }

# print(banka["sinan"]["bakiye"])


def hesapvarmi(isim):    
    if isim in banka :
        return True
    else : 
        return False




while True :
    print("Lütfen bir seçim yapınız. ")
    print("1 : bakiye öğren ")
    print("2 : Para çek ")
    print("3 : Para yatır ")
    secim = input("Çıkış yapılsın mı (e/h) : ")
    if secim.lower() == "e" :
        break
    elif secim.lower() == "1" :
        ad = input("isim girin")
        bakiye = input("bakiye girin")
        ekhesap = input("ek hesap istiyor musunuz")
        banka.appen({
            "isim" : ad,
            "bakiye" : bakiye,
            "ekhesap" : 5000,
        })
    elif secim.lower() == "2" :
        isim = isim = input("isim girin : ")
        if hesapvarmi(isim) :
            print("bakiyeniz")

"""

