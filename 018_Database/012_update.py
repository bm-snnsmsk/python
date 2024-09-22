import mysql.connector


def updateProduct() :
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "Password1234", auth_plugin='mysql_native_password', database='node_app')
    cursor = conn.cursor()
    
    sorgu = "UPDATE products SET name = 'blacberry', price=25000 WHERE id = 5 " 
    
    
    cursor.execute(sorgu)    

    try :
        conn.commit() 
        print(f"{cursor.rowcount} tane kayıt güncellendi.")  
        print(f"Son güncellenen kaydın id : {cursor.lastrowid}")
        
    except Exception as err :
        print(f"Hata : {err}")
    finally :
        conn.close()



updateProduct()