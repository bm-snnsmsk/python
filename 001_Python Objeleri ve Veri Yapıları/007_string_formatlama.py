name = "sinan"
surname = "şimşek"
age = 39

# selamlama = "benim adım "+ name + " " + surname +" ve " + str(age) + " yaşındayım"




print("benim adım {}".format(name))
print("benim adım {} {}".format(name, surname))
print("benim adım {1} {0}".format(name, surname))
print("benim adım {a} {s} {n}".format(n=name, s=surname, a=age))

print(f"benim adım {name} {age} {surname}")


### sonuç 0.454512121212 tam kısmı 0 ise 0.2 işe yarar, aksi takdirde tam sayıyı hesaplar kalan kısmı ondalık gösterir
result = 200 / 700
print("sonuc : {r}".format(r=result))
print("sonuc : {r:1.3}".format(r=result))   # 0.286
print(f"sonuc : {result:1.3}")   # 0.286
print(f"{result:1.4}")   //// soldaki için de kaç basamaklık alan ayırsın
print(f"{result:0.6}")
print(f"{result:8.6}")


"""
uygulama
course = "sinan şimşek"  >>> tersetn yazdırma

print(len(course))    //// toplam karakter sayısı
print(course[::-1])
print(course[-5:])    /// -5 den sona doğru
print(course[-5:-2])
print(course[-5::-1])  /// -5 den iitbaren tersten yazdır
print("abc"*3)     /// abcabcabc

"""
