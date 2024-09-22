import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",  ## 192.23.45.56  ## hosting kiralanaksa alınacak örnek adres
    user = "root",
    password = "Password1234",
    auth_plugin='mysql_native_password', ## şifre çözümleme hatası bu kodla giderildi
    database='schooldb'
)

mycursor = mydb.cursor()

# mycursor.execute("show databases")
# for i in mycursor :
#     print(i)

def inserDatas(datas):    
    sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
    values = datas
    mycursor.executemany(sql, values)

    try : 
        mydb.commit()
        print(f"{mycursor.rowcount} tane kayıt eklendi")
    except Exception as err :
        print(f"Hata : {err}")
    finally : 
        mycursor.close()


liste = []
liste.append(("108","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"))
liste.append(("109","ali","can",datetime.datetime(2005, 6, 17), "E"))
liste.append(("110","canan","tan",datetime.datetime(2005, 7, 7), "K"))
liste.append(("111","ayşe","taner",datetime.datetime(2006, 9, 23), "K"))
liste.append(("112","bahadır","toksöz",datetime.datetime(2004, 7, 27), "E"))
liste.append(("113","ali","cenk",datetime.datetime(2003, 8, 25), "E"))

inserDatas(liste)


