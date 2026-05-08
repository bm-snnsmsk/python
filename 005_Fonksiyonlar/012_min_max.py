sayilar = [1,6,7,14,9,11]
harfler = ["a","h","r","w"]
isimler = ["sinan","kenan","elif"]


sonuc = min([len(i) for i in isimler])
sonuc = max(isimler, key = lambda i : len(i))


print(sonuc)



urunler = [
    {"title":"samsung s23", "price": 70000},
    {"title":"samsung s24", "price": 80000},
    {"title":"samsung s25", "price": 90000}
]

sonuc = min(urunler, key = lambda urun: urun["price"])
sonuc = max(urunler, key = lambda urun: urun["price"])["title"]

max = 0

for urun in urunler:
    if(urun["price"] > max):
        max = urun["price"]

print(max)

print(sonuc)
# sonuc = max(isimler, key = lambda i : i["price"])
# sonuc = max(isimler, key = lambda i : i["price"]["title"])
