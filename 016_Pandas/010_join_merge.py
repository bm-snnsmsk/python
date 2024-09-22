import pandas as pd

## join
# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner")  ## iki küme birleşimi
# result = pd.merge(df_customers,df_orders,how="left") ## soldaki tüm veriler ayrıca birleşim varsa onları da getir, siparişi yoksa NaN gelir
# result = pd.merge(df_customers,df_orders,how="right") ## sağdaki tüm veriler ayrıca birleşim varsa onları da getir, müsteiler yoksa NaN gelir
# result = pd.merge(df_customers,df_orders,how="outer") ## sağdaki ve soldaki tüm veriler ayrıca birleşim varsa onları da getir, olmayan veriler NaN gelir

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])


## benzer kolonlar varsa concat yapılır
# result = pd.concat([df_customersA,df_customersB]) ## alt alta ekler 
# result = pd.concat([df_customersA,df_customersB], axis=0) ## alt alta ekelr
result = pd.concat([df_customersA,df_customersB], axis=1) ## yan yana ekelr



print(result)