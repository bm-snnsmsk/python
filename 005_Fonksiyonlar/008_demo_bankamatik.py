hesapSinan = {
    "ad" :"Sinan Şimşek",
    "hesapNo" :"123456",
    "bakiye" :3000,  ## dictionary olduğu için günceleme yapılır
    "ekHesap" :2000,
} # value değer olsaydı mevcut değerler üzerinde güncelleme yapılmazdı
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



