# open(dosya_adi, mod)

# mod

# "w"  yazma modu. dosya mevcut ise eski bilgiler silinir.
# "a"  ekleme yapar. dosya varsa ekleme yapar dosya konumda yoksa oluşturur
# "x"  oluşturma.dosya varsa hata verir, dosya konumda yoksa oluşturur
# "r" okuma. dosya konumda yoksa hata verir

file = open("Dosyalar/newfile.txt", "w", encoding="utf-8")
file.write("dosyaya yazı yazıldı...")  ## ilgili dosyaya içerik ekler
print(file)    ### <_io.TextIOWrapper name='newfile.txt' mode='w' encoding='utf-8'>
file.close()   ## dosya açık kalırsa kaynak tüketir, makineyi yorar. o yüzden kapatılması gerekir
########################################3

f = open("newfile.txt", "w", encoding="utf-8")
f.write("dosyaya içerik eklendi...")  ## ilgili dosyaya içerik ekler
f.close() 
