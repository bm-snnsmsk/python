liste1 = [1,2,3,4,5]
liste2 = ["a","b","c","d","e"]
liste3 = ["+","-","*","/","#"]

tumliste = list(zip(liste1, liste2))   #### eşleştirerek birleştirme yapar [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]
tumliste2 = list(zip(liste1, liste2, liste3))

print(tumliste)
print(tumliste2)

for item in tumliste2 :
    print(item)


for a,b,c in tumliste2 :
    print(a,b,c)


