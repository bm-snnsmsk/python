liste = [1, "iki", 3]
tuple = (1, "iki", 3)

# liste = []
# dictionary = {}
# tuple = ()


print(type(liste))
print(type(tuple))


# liste[0] = 200      # gibi bir güncelleme listelerde yapılabilir
# tuple[0] = 200      # gibi bir güncelleme tuple yapılamaz

tuple + (60, 78, "sinan")
# listede geçerli bu metotlar tuple için de geçerlidir başka da yok
tuple.count(3)
tuple.index(3)

## tuple, list'den hafızada daha az yer kaplar
## bu yüzden projede değiştirilmeyecek olan değerler tuple olarak gösterilirse kasma az olur

