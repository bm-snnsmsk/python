fruits = { "orange","apple","banana"}

# print(fruits[0])   # indexlenemezler

for i in fruits : 
    print(i)

fruits.add("cherry")
fruits.update(["mango","grape","apple"])  ## apple zeten listede olduğu için bir daha eklenemez

print(fruits)

liste = [1, 2, 2, 3, 7, 3, 9, 7]
print(set(liste))    # set listeleri her elemanı bir defa gösterir

fruits.remove("mango")
fruits.discard("apple")

print(fruits)

fruits.pop()  ## set listeelerinde son elemanı silmeyi garanti etmez
print(fruits)

fruits.clear()  # tüm elemanlar silinir