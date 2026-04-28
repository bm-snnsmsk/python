# https://dev.mysql.com/downloads     >>> bu sayfada server kur
# https://dev.mysql.com/downloads/workbench/     ### aynı sayfada arayüz progrmı olan mysql bench kur
## pip install mysql-connector

import mysql.connector



mydb = mysql.connector.connect(
    host = "localhost",  ## 192.23.45.56  ## hosting kiralanaksa alınacak örnek adres
    user = "root",
    password = "Password1234",
    auth_plugin='mysql_native_password' ## şifre çözümleme hatası bu kodla giderildi
)

# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")  ## DB oluşturma

mycursor.execute("show databases")

for i in mycursor :
    print(i)
