from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/"

# network / headers / user agent
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content # 403 forbidden hatası almamak için
# print(html)

soup = BeautifulSoup(html, "html.parser")
# print(soup)
# liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li", limit=1)
liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li")
# print(liste)

for i in liste : 
    filmadi = i.find("h3", {"class":"ipc-title__text"}).text
    puan = i.find("span", {"class":"ipc-rating-star"}).text
    print(filmadi, puan)