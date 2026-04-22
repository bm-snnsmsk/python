name = "Sinan Şimşek"

print("break".center(50,"*"))
for i in name :
    if i == "n" :
        break
    print(i)


print("continue".center(50,"*"))
for i in name :
    if i == "n" :
        continue
    print(i)

################# 
i = 0
while True :
    i += 1          #### artırma azaltma ilk satırda olmazsa hata verir

    if i == 100 :
        break
    
    if i % 2 == 1 :
        continue
    print(f"sayı : {i}") 





