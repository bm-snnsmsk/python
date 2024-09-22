import mysql.connector

# def insertProduct() :
#     conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
#     cursor = conn.cursor()
    
#     sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
#     values = ("Samsun s20", 17000, "3.jpg", "yeni telefon")

#     cursor.execute(sql, values)

#     try :
#         conn.commit()  ## sorguyu database'e gönder
#     except Exception as err :
#         print(f"Hata : {err}")
#     finally :
#         conn.close()
#         print("Database bağlantısı kapatıldı.")

# insertProduct()


#### tek ürün ekleme
def insertProduct(name, price, imageUrl, description) :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)

    try :
        conn.commit()  ## sorguyu database'e gönder
        print(f"{cursor.rowcount} tane kayıt eklendi.")  
        print(f"Son eklenen kaydın id : {cursor.lastrowid}")  
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()
        print("Database bağlantısı kapatıldı.")


# name = "iphone 11"
# price = 23000
# imageUrl = "6.jpg"
# description = "güzel ürün"

# insertProduct(name, price, imageUrl, description)


# birden fazla eleman ekleme
def insertProducts(liste) :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = liste

    cursor.executemany(sql, values)

    try :
        conn.commit()  ## sorguyu database'e gönder
        print(f"{cursor.rowcount} tane kayıt eklendi.")  
        print(f"Son eklenen kaydın id : {cursor.lastrowid}")  
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()
        print("Database bağlantısı kapatıldı.")


liste = []
while True :
    name = input("ürün adı : ")
    price = input("ürün fiyat : ")
    imageUrl = input("ürün foto : ")
    description = input("ürün açıklama : ")

    #  insertProduct(name, price, imageUrl, description) ## bu da yapılabilir ama sürekli DB aç-kapat yapmak gerekecektir. liste halide göndermek bu işlemi tek seferde aç-kapat yapacaktır. bu daha işlevsel olacaktır. 
    liste.append((name, price, imageUrl, description))

    secim = input("devam etmek istiyor musunuz (e/h) ? :")
    if secim == "h" :
        print("kayıtlar kaydediliyor...")
        print(liste)
        insertProducts(liste)
        break




