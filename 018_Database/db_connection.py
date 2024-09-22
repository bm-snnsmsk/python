import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",  ## 192.23.45.56  ## hosting kiralanaksa alınacak örnek adres
    user = "root",
    password = "Password1234",
    auth_plugin='mysql_native_password', ## şifre çözümleme hatası bu kodla giderildi
    # database='schooldb'
    database='okuldb'
)
