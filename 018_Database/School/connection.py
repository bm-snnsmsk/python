import mysql.connector 

connection = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "Password1234",
    auth_plugin='mysql_native_password',
    database='okuldb'
)
