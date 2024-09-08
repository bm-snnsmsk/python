## with bloğu kullanılınca file.close() ile dosya kapatmaya gerek yok

# with open("Dosyalar/newfile.txt","r", encoding="utf-8") as file :
#     icerik = file.read()
#     print(icerik)
#     print(file.tell())  ## cursor nerde
#     print(icerik)

with open("Dosyalar/newfile.txt","r", encoding="utf-8") as file :
    icerik = file.read()
    print(icerik)
    print(file.seek(10))   ## cursor belirtilen byte'a gönderilir
    print(file.tell())  ## cursor nerde
    icerik2 = file.read()
    print(icerik2)
