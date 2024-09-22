import mysql.connector


def getProducts() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sql = "SELECT * FROM products ORDER BY name" ## artan
    sql = "SELECT * FROM products ORDER BY price"  ## artan
    sql = "SELECT * FROM products ORDER BY price ASC"  ## artan
    sql = "SELECT * FROM products ORDER BY price DESC" ## azalan
    sql = "SELECT * FROM products ORDER BY name, price" ## önce name' göre sırala, grupla sonra her price'a göre sırala
    
    cursor.execute(sql)
    

    try :
        urunler = cursor.fetchall() 
        for i in urunler :
            print(f"id : {i[0]} - urun adı : {i[1]} ---- urun fiyatı : {i[2]}")
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



getProducts()