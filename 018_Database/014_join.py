import mysql.connector


def getProducts() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sql = "SELECT * FROM products"
    sql = "SELECT * FROM categories"
    # sql = "SELECT * FROM products WHERE id<10 and id>2"
    ### inner join sadece keşisim olan seçimler
    sql = "SELECT * FROM products INNER JOIN categories ON categories.id=products.categoryid"
    sql = "SELECT * FROM products INNER JOIN categories ON categories.id=products.categoryid WHERE categories.name = 'telefon'"
    sql = "SELECT products.name, products.price, categories.name FROM products INNER JOIN categories ON categories.id=products.categoryid WHERE categories.name = 'telefon'"
    sql = "SELECT p.name, p.price, c.name FROM products AS p INNER JOIN categories AS c ON c.id=p.categoryid WHERE c.name = 'telefon'"
    
    cursor.execute(sql)
    

    try :
        urunler = cursor.fetchall() 
        for i in urunler :
            print(f"{i}")
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



getProducts()