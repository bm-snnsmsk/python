print("range(10)".center(50,"*"))
for i in range(10) :
    print(i)

print("range(3,10)".center(50,"*"))
for i in range(3,10) :
    print(i)


print("range(3,10,2)".center(50,"*"))
for i in range(3,10,2) :
    print(i)

print("list(range(5,100,10))".center(50,"*"))
print(list(range(5,100,10)))      ### list(range(5,100,10)) listeye çevirme

print("list(range(50,10))".center(50,"*")) # 50'den geriye sayar
for i in range(50,10, -2) :    ### ilk sayı ikinci sayıdan büyükse eğer - bir değerle artırma yazılmalı yoksa çalışmaz
    print(i)

print("list(range(50,10))".center(50,"*")) # 15'den 3'e kadar 4 azalarak geriye sayar
for i in range(15,3,-4) :
    print(i)





