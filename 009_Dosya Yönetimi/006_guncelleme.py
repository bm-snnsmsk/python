# with open("Dosyalar/newfile.txt","r+", encoding="utf-8") as file :
#     file.write("yeni eklemeler yapıldı")  # ama başa ekleme yapıldı
#     icerik = file.read()
#     print(icerik)

######################################################################
# # sayfa sonuna ekleme yapar
# with open("Dosyalar/newfile.txt","a", encoding="utf-8") as file :
#     file.write("en sona ekleme yapılma test ediliyor")

# with open("Dosyalar/newfile.txt","r", encoding="utf-8") as file :
#     print(file.read())

# ######################################################################
# # sayfa başına ekleme yapar
# with open("Dosyalar/newfile.txt","r+", encoding="utf-8") as file :
#     icerik = file.read()
#     icerik = "sinan şimşek\n" + icerik
#     file.seek(0)
#     file.write(icerik)

# with open("Dosyalar/newfile.txt","r", encoding="utf-8") as file :
#     print(file.read())         
          
######################################################################
# sayfa ortasına ekleme yapar
with open("Dosyalar/newfile.txt","r+", encoding="utf-8") as file :
    satirlar = file.readlines()
    satirlar.insert(3,"tuba nur şimşek\n")
    file.seek(0)

    # for i in satirlar :
    #     file.write(i)    ## tek satır ekleme yapar

    file.writelines(satirlar)   ## tüm satırları ekler


with open("Dosyalar/newfile.txt","r", encoding="utf-8") as file :
    print(file.read())         
          
######################################################################