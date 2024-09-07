sayi = int(input("bir sayı gir : "))

dict = []

i = 0 
while i < sayi :
    name = input("ürün ismi gir : ")
    price = int(input("ürün fiyatı gir : "))
    dict.append({"name":name, "fiyat":price})
    i += 1


print(dict)

i = 0
while i < sayi :  
    print(f'{dict[i]["name"]} --- {dict[i]["fiyat"]}')
    i += 1





