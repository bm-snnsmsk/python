mesaj = "Hello There. My name is Sinan Şimşek"
mesaj2 = " Hello There. My name is Sinan Şimşek "

print(mesaj.upper())
print(mesaj.lower())
print(mesaj.title())    /// her kelimenin ilk harfi büyük 
print(mesaj.capitalize())   /// cümlenin ilk harfi büyük

print(mesaj2)
print(mesaj2.strip())  # başta ve soldaki boşlukları siler
print(mesaj2.strip("H"))  # başta H'yi siler
print(mesaj2.strip("Hel"))  # başta Hel'yi siler
print(mesaj2.lstrip())  # baştaki boşlukları siler
print(mesaj2.rstrip())  # sağdaki boşlukları siler
print("e'ler silinsin : "+mesaj2.lstrip("He"))  #  siler        ### silemedim

print(mesaj.split())    # stringi boşluklardan diziye dönüştürür
print(mesaj.split(" "))    # stringi boşluklardan diziye dönüştürür
print(mesaj.split("."))    # stringi noktalardan diziye dönüştürür
print(mesaj.split()[3])    # stringi diziye dçönüştürür ve 3. indexteki elemanı verir
print("".join(mesaj.split()))    # diziye stringe dönüştürür
print(" ".join(mesaj.split()))    # diziye stringe dönüştürür
print("#".join(mesaj.split()))    # diziye stringe dönüştürür
print("---".join(mesaj.split()))    # diziye stringe dönüştürür

print(mesaj.find("T"))    # index numarasını verir
print(mesaj.find("sinan"))    # sinan arar ve s'nin index numarasını verir
print("snn" in mesaj)    # true false
print("snn" not in mesaj)    # true false
print(mesaj.rfind("T", 10,15))    # sağdan ara index numarasını verir
print(mesaj.find("There"))    # bulduğu ilk kelimenin index numarasını verir
print(mesaj.find("baran"))    # -1     bu kelime yok

print(mesaj.startswith("H"))    # True
print(mesaj.endswith("H"))    # False

print(mesaj.replace("Sinan","baran"))    # Hello There. My name is baran Şimşek
print(mesaj.replace("","*"))    # *H*e*l*l*o* *T*h*e*r*e*.* *M*y* *n*a*m*e* *i*s* *S*i*n*a*n* *Ş*i*m*ş*e*k*
print(mesaj.replace(" ",""))    # HelloThere.MynameisSinanŞimşek
print(mesaj.replace("","*",5))    # *H*e*l*l*o There. My name is Sinan Şimşek
print(mesaj.replace(" ","*"))    # Hello*There.*My*name*is*Sinan*Şimşek
print(mesaj.replace("e","E").replace("a","A").replace(" ","-"))    #HEllo-ThErE.-My-nAmE-is-SinAn-ŞimşEk


print(mesaj.center(50))
print(mesaj.center(50,"*"))
print(mesaj.ljust(50,"*"))
print(mesaj.rjust(50,"*"))

print(mesaj.count("e"))
print(mesaj.count("www"))
print(mesaj.count("sinan"))
print(mesaj.count("e",0,5))   # 0,5 aralığında bul say

# print(mesaj.index("ç"))
# print(mesaj.isdecimal())
# print("5".isdecimal())
# print("s".isdecimal())
# print("48".isascii())
# print("G".isupper())


# name = "Sinan Şimşek"
# phone = "05444494263"
# print(name.lower())
# print(name.upper())
# print(name.endswith("k"))
# print(name.endswith("Şimşek"))
isim = "Sinan Şimşek ağlamak öğrenci üşümek çağrı"
# print(isim.replace("[çğıöşü]", "[ÇĞIÖŞÜ]"))
# print(isim.replace("ç", "Ç"))


print(mesaj.index("Hello"))
print(mesaj.rindex("Hello"))    /// find ile aramada aranan yoksa -1 döndürür ama index() aranan değer buunmazsa hata fırlatır

print(mesaj.isalpha())   # false
print(mesaj.isdigit())   # false

email = " sNn@GmAil.com"
print(email)



tüm stringler >>>
https://www.w3schools.com/python/python_ref_string.asp

"""
website = "http://www.sinansimsek.com"
website2 = "www.sinansimsek.com"

print(website.lstrip("http://"))
print(website2.strip("w.com"))

###################################################################
deger = "sinan baran emine pelda rizgar arami demhat rojhat"
print(deger.replace("a","A"))   /// hepsini değiştir
print(deger.replace("a","A",3))   // ilk 3 tanesini değiştir
###################################################################

###################################################################
name = "sinan"
print(name.split())     >>> tek kelimelik liste
print(list(name))       >>> tüm karakterleri listeye çevirir
###################################################################



"""


print(email.strip().lower())
