import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",  ## 192.23.45.56  ## hosting kiralanaksa alınacak örnek adres
    user = "root",
    password = "Password1234",
    auth_plugin='mysql_native_password', ## şifre çözümleme hatası bu kodla giderildi
    database='mydatabase'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")  
