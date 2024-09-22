import pandas as pd


data = pd.read_csv("DataSets/nba.csv")

# data.dropna()
data.dropna(inplace = True)
# data["Name"] = data["Name"].str.upper() ## isim alanları büyük yap
# data["Name"] = data["Name"].str.lower() ## isim alanları küçük yap
# data["index"] = data["Name"].str.find('a') ## index adındfa bir kolon yap belirlelnen depeğerleri ekle
# data = data.Name.str.contains('Jordan')  ## içinde Jordan geçen kelimeler
# data = data[data.Name.str.contains('Jordan')]   ## içinde Jordan geçen satırlar
# data = data.Team.str.replace(' ','-')
# data = data.Team.str.replace(' ','-').str.replace("","*")
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True) ## isim-soyisim adında bir alan oluştur, name adındaki boşluklardan böl, ve iki kelimeden oluşuyorsa, böl ayrı ayrı kolonlara ekle  





# print(data)
print(data.head(10))