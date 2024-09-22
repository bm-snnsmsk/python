import mysql.connector


def getProducts() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sql = "SELECT * FROM products LIMIT 4"
    sql = "SELECT * FROM products "
    sql = "SELECT * FROM products WHERE id > 2 and id < 6"
    sql = "SELECT * FROM products WHERE price > 10000 or id < 6"
    sql = "SELECT * FROM products WHERE name = 'Samsung s7' "     ## büyük-küçük harf duyarlığı yok
    sql = "SELECT * FROM products WHERE name = 'samsung s7' "     ## büyük-küçük harf duyarlığı yok
    sql = "SELECT * FROM products WHERE name LIKE  '%samsun%' "   ## içinde samsun geçen kelimeler
    sql = "SELECT * FROM products WHERE name LIKE  'samsun%' "   ## başı samsun olan
    sql = "SELECT * FROM products WHERE name LIKE  '%samsun' "   ## sonu samsun olan
    sql = "SELECT * FROM products WHERE name LIKE  '%samsun%' and price = 17000 "   
    cursor.execute(sql)
    

    try :
        # tek_urun = cursor.fetchone()  ## tek kayıt - ilk kayıt
        urunler = cursor.fetchall() 
        # print(tek_urun)
        for i in urunler :
            print(f"id : {i[0]} - urun adı : {i[1]} ---- urun fiyatı : {i[2]}")
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



getProducts()