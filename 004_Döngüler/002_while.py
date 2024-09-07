x = 0 

while x < 100 :
    if x % 5 == 0 :
        print(x)
    x+=1
print("while bitti...")


name = ""
while not name.strip() :
    name = input("isim giriniz : ")
print(f"adınız : {name}")
