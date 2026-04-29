import mysql.connector

# ALTER TABLE products
# ADD CONSTRAINT fk_categories_products
# FOREIGN KEY (categoryid) REFERENCES categories(id)

# products ayar sayfasında foreing key alanında on update veya on delete den sonra 
# restric(varsayılan değer silmeyi engeller), 
# cascade (ilşkili veriler de silinsin), 
# set null(ilişkili derğerler null olarak belirlenmiş olacaktır ama en bata model tasarlanmasında prodeucts tablosunda categoryid alanı 
# NN(not null seili olmaması lazım null değerini kabul etmesi gerekir)
seçeneklerinden biri seçilebilir


## inner join   >>> keşisim
## left join   >>> keşisim + soldaki küme
## right join   >>> keşisim + sağdaki küme
## full outer join   >>> keşisim + her iki küme


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
