# open(dosya_adi, mod)

# mod

# "w"  yazma modu. dosya mevcut ise eski bilgiler silinir.
# "a"  ekleme yapar. dosya varsa ekleme yapar dosya konumda yoksa oluşturur
# "x"  oluşturma.dosya varsa ekleme hata verir dosya konumda yoksa oluşturur
# "r" okuma. dosya konumda yok hata verir


dosya_name = "Dosyalarwww/newfile.txt"   ## dosya olmadığından hata verecektir
dosya_name = "Dosyalar/newfile.txt"
try :
    file = open(dosya_name, "r", encoding="utf-8")



######## Dosya Okuma 1 #####################################
    # for i in file :
        # print(i) # her satır sonunda bir satır ekler
        # print(i, end="") # her satır sonunda boş satır eklemez
######## Dosya Okuma 2 #####################################
    # print(file.read())   ## imlec en sona geçer. dosya kapaılmadan önce bir kez daha okumayapılcaksa, boş içerik gönderirir.
######## Dosya Okuma 2 #####################################
    # print(file.read(15))    ## size : okunacak karakter sayısı
######## Dosya Okuma 2 #####################################
    # print(file.readline())    ## tek satır okunur
    # print(file.readline(), end="")    ## tek satır okunur
######## Dosya Okuma 2 #####################################
    print(file.readlines())    ## tüm içeriği her satır bir eleman olacak şekilde diziye çevirir





except FileNotFoundError as err:
    print(err)
finally :
    file.close()

