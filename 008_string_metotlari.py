mesaj = "Hello There. My name is Sinan Şimşek"
mesaj2 = " Hello There. My name is Sinan Şimşek "

print(mesaj.upper())
print(mesaj.lower())
print(mesaj.title())
print(mesaj.capitalize())

print(mesaj2)
print(mesaj2.strip())  # başta ve soldaki boşlukları siler
print(mesaj2.lstrip())  # baştaki boşlukları siler
print(mesaj2.rstrip())  # sağdaki boşlukları siler
print("e'ler silinsin : "+mesaj2.lstrip("He"))  #  siler        ### silemedim

print(mesaj.split())    # stringi diziye dönüştürür
print(mesaj.split())    # stringi diziye dönüştürür
print(mesaj.split()[3])    # stringi diziye dçönüştürür ve 3. indexteki elemanı verir
print("".join(mesaj.split()))    # diziye stringe dönüştürür
print(" ".join(mesaj.split()))    # diziye stringe dönüştürür
print("#".join(mesaj.split()))    # diziye stringe dönüştürür
print("---".join(mesaj.split()))    # diziye stringe dönüştürür

print(mesaj.find("T"))    # index numarasını verir
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
print(mesaj.count("e",0,5))   # 0,5 aralığında bul say



print(mesaj.index("Hello"))
print(mesaj.rindex("Hello"))

print(mesaj.isalpha())   # false
print(mesaj.isdigit())   # false