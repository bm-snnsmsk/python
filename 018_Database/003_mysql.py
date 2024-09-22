import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",  ## 192.23.45.56  ## hosting kiralanaksa alınacak örnek adres
    user = "root",
    password = "Password1234",
    auth_plugin='mysql_native_password' ## şifre çözümleme hatası bu kodla giderildi
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")  ## DB oluşturma

mycursor.execute("show databases")

for i in mycursor :
    print(i)