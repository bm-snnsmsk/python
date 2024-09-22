import mysql.connector


def getProductById(id) :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sql = "SELECT * FROM products WHERE id=%s"
    parametre = (id,)
     
    cursor.execute(sql, parametre)
    

    try :
        tek_urun = cursor.fetchone()  ## tek kayıt - ilk kayıt
        print(tek_urun)
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



getProductById(2)