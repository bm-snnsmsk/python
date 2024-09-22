import mysql.connector


def deleteProduct() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sorgu = "DELETE FROM products WHERE id = 2 " 
    sorgu = "DELETE FROM products WHERE name LIKE '%s20%' " 
        
    cursor.execute(sorgu)    

    try :
        conn.commit() 
        print(f"{cursor.rowcount} tane kayıt silindi.")  
        print(f"Son silinen kaydın id : {cursor.lastrowid}")
        
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



deleteProduct()