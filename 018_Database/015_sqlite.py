import sqlite3

conn = sqlite3.connect("chinook.db")  ## varsa böyle bir dizin gider bağlanır mevcut değilse önce kurar sonra bağlanır
curs = conn.cursor()

sql = "SELECT * FROM albums"
curs.execute(sql)

result = curs.fetchall()

for i in result :
    print(i[1])


conn.close()