import mysql.connector


def getProducts() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    # sql = "SELECT * FROM products"
    sql = "SELECT name, price FROM products"

    cursor.execute(sql)
    

    try :
        ilk_urun = cursor.fetchone() 
        urunler = cursor.fetchall() 
        print(f"############ ilk ürün #####################")
        print(f"ilk urun : {ilk_urun}")
        print(f"############ diğer ürünler #####################")
        for i in urunler :
            # print(f"urun adı : {i[1]} ---- urun fiyatı : {i[2]}")  
            print(f"urun adı : {i[0]} ---- urun fiyatı : {i[1]}")  
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()
        print("Database bağlantısı kapatıldı.")



getProducts()