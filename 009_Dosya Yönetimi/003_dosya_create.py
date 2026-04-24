# open(dosya_adi, mod)

# mod

# "w"  yazma modu. dosya mevcut ise eski bilgiler silinir.
# "a"  ekleme yapar. dosya varsa ekleme yapar dosya konumda yoksa oluşturur
# "x"  oluşturma.dosya varsa hata verir, dosya konumda yoksa oluşturur
# "r" okuma. dosya konumda yoksa hata verir

file = open("Dosyalar/newfile.txt", "x", encoding="utf-8")
print(file)    ## dosya nevcut olduğu için hata verecektir.
file.close()

