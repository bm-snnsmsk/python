import mysql.connector


def getProducts() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sorgu = "SELECT COUNT(*) FROM products" 
    sorgu = "SELECT COUNT(name) FROM products" ## yukardaki ile aynı
    sorgu = "SELECT COUNT(*) FROM products WHERE price > 10000" ## şartı sağlayan kayıt sayısı
    sorgu = "SELECT AVG(price) FROM products" ## ortalama
    sorgu = "SELECT AVG(price) FROM products WHERE price > 10000" ## şartı sağlayan kayıtların ortslaması
    sorgu = "SELECT SUM(price) FROM products" ## toplamı
    sorgu = "SELECT MAX(price) FROM products" ## max
    sorgu = "SELECT MIN(price) FROM products" ## min
    sorgu = "SELECT name, price FROM products WHERE price = (SELECT MAX(price) FROM products)" ## 
    # "SELECT * FROM student WHERE YEAR(birthdate) = 2003"
    ### ayrıca YEAR, DAY, MONTH gibi tarih metotları da var
    

    cursor.execute(sorgu)    

    try :
        result = cursor.fetchone() 
        print(result)
        
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



getProducts()