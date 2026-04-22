x = 0 

while x < 100 :
    if x % 5 == 0 :
        print(x)
    x+=1
print("while bitti...")

#########################
name = ""
while not name.strip() :
    name = input("isim giriniz : ")
print(f"adınız : {name}")


#########################
a = 0
cift = 0
tek = 0
while True :
    if a == 13 :
        break
    
    if a % 2 == 0 :
        cift += 1
        print(f"{a} : çift")
    elif a % 2 == 1 :
        tek += 1
        print(f"{a} : tek")
    a += 1
    ############################

  
print(f"çift sayısı : {cift} >>> tek sayısı : {tek}")
