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

kume1 = {1,2,3,4,5}
kume2 = {1,2,6,9,5}
print(kume1|kume2)   ## birleşim kümesi -  1,2,3,4,5,6,9
print(kume2|kume1)   ## birleşim kümesi -  1,2,3,4,5,6,9
print(kume1 & kume2)   ## kesişim kümesi -  1,2,5
print(kume1 - kume2)   ## kume1 fark kume2 -  3,4
print(kume2 - kume1)   ## kume2 fark kume1 -  6,9
