import re
# regular expression 

# result = dir(re)


str = "Sinan Şimşek : Bilgisayar Sinan Mühendisi | Mardin İl Sağlık Müdürlüğü"


# result = re.findall("Sinan", str) ## kaç tane kelime ?

# result = re.split(" ") ## boşluktan veya belirtilecek başka bir karakterden böler

# result = re.sub(" ","-", str) ## değiştirme # re.sub("\s","-", str)
# result = re.sub("a","-", str) ## değiştirme

# result = re.search("Sinan", str) # ilk değeri match objesi döndürür
# result = re.search("Sinan", str).span() # bulunduğu indis aralığı 
# result = re.search("Sinan", str).start() # başlangıç indis  
# result = re.search("Sinan", str).end() # bitiş indis  
# result = result.group() ## Sinan
# result = result.string   ## tüm ifade

result = re.findall("[abc]", str)   ## karakterler
result = re.findall("[a-z]", str)
result = re.findall("[^a-z]", str)
result = re.findall("[0-9]", str)
result = re.findall("[^0-9]", str)
result = re.findall("[0-395]", str) # 012395
result = re.findall("[a-zA-Z0-9]", str)
result = re.findall(".", str)  ## herhangi bir karakter
result = re.findall("..", str)  ## iki basamaklı karakter
result = re.findall("...", str)  ## üç basamaklı karakter
result = re.findall("Pyt..on", str)  ## Pyt(a-z)(a-z)on
result = re.findall("^a", str)  ## str ifadesi a ile başlayıyor mu 
result = re.findall("a$", str)  ## str a ile bitiyor mu 
result = re.findall("ma*n", str)  ## a 0 ya da daha fazla var mı
result = re.findall("ma+n", str)  ## a 1 ya da daha fazla var mı
result = re.findall("ma?n", str)  ## a 0 veya 1 tane var mı
result = re.findall("san{2}", str)  ## an 2 tane
result = re.findall("san{2, 5}", str)  ## an en az 2 en fazla 5 tane
result = re.findall("[0-9]{2, 5}", str)  ## rakamlar en az 2 en fazla 5 tane
result = re.findall("a|b", str)  ## a ya da b
result = re.findall("(a|b|c)xz", str)  ## a ya da b ya da c ile başlayan xz ile biten
result = re.findall("\$a", str)  ## kaçış \ burda $a ile başlayan
result = re.findall("\A", str)  ## en başında
result = re.findall("\Asnn", str)  ## en başında snn var mı
result = re.findall("\bsnn", str)  ## kelimelerin başında snn var mı
result = re.findall("snn\b", str)  ## kelimelerin sonunda snn var mı
result = re.findall("\Bsnn", str)  ## kelimelerin başında snn var mı
result = re.findall("snn\B", str)  ## kelimelerin sonunda snn var mı
result = re.findall("\d", str)  ## [0-9]
result = re.findall("\D", str)  ## [^0-9]
result = re.findall("\s", str)  ## boşluk
result = re.findall("\S", str)  ## boşluk dışındakiler
result = re.findall("\w", str)  ## alfabetik, rakam ve _
result = re.findall("\W", str)  ## alfabetik, rakam ve _ dışındakiler



print(result)
