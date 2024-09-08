# open(dosya_adi, mod)

# mod

# "w"  yazma modu. dosya mevcut ise eski bilgiler silinir.
# "a"  ekleme yapar. dosya varsa ekleme yapar dosya konumda yoksa oluşturur
# "x"  oluşturma.dosya varsa ekleme hata verir dosya konumda yoksa oluşturur
# "r" okuma. dosya konumda yok hata verir

file = open("Dosyalar/newfile.txt", "a", encoding="utf-8")
# file.write("dosyaya ekleme yapıldı")
file.write("dosyaya ekleme yapıldı\n")
file.close()

