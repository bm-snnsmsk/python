from bs4 import BeautifulSoup
import requests

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

# network / headers / user agent
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
# n11 de de aynı çünkü aynın pc aynı tarayıcı
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36

html = requests.get(url, headers=headers).content # 403 forbidden hatası almamak için
# print(html)

soup = BeautifulSoup(html, "html.parser")
# print(soup)
liste = soup.find_all("li", {"class":"column"}, limit=1)
# liste = soup.find_all("li", {"class":"column"})
# print(liste)

for i in liste : 
    link = i.a.get("href") # li altında a
    product_name = i.a.h3.text # li altında a altında h3
    image = i.find("img", {"class":"cardImage"}).get("data-images").split(",") # image'lar
    fiyat = i.find("div", {"class":"priceContainer"}).find_all("span")[-1].ins.text.strip("TL")

    # print(link)
    # print(product_name)
    # print(image) 
    print(fiyat) 