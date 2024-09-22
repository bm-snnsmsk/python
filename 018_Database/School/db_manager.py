import mysql.connector 
import datetime 
from connection import connection
from student import Student
from teacher import Teacher
from ders import Class


class DbManager :
    def __init__(self) :
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_students_by_class_id(self, classid) :
        sql = "SELECT * FROM student WHERE classid=%s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try :
            ogr = self.cursor.fetchall()
            return Student.CreateStudent(ogr) 
           
        except Exception as err:
            print(f"Hata : {err}")

    def get_student_by_id(self, id) :
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try :
            ogr = self.cursor.fetchone()
            return Student.CreateStudent(ogr)
        except Exception as err:
            print(f"Hata : {err}")

    def add_student(self, student:Student) :
        sql = "INSERT INTO student (student_number,name,surname,birthdate,gender,classid) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.student_number,student.name, student.surname,student.birth_date,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def edit_student(self, student) :
        sql = "update student set student_number=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.student_number,student.name, student.surname,student.birth_date,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err) 

    def delete_student(self,studentid):
        sql = "DELETE FROM student WHERE id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi...')
        except mysql.connector.Error as err:
            print('hata:', err)

    def add_Teacher(self, teacher) :
        pass

    def edit_Teacher(self, teacher) :
        pass

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    # def __del__(self) :
    #     self.connection.close()
    #     print("DB kapandı...")



# db = DbManager()

######### select TEST
# result = db.get_student_by_id(2)
# print(result.name)
# print(db.get_student_by_id(2))
# print(db.get_students_by_class_id(1)[0].name)


######### insert TEST
# t = '21 April 2019 hour 20:42:18'
# dt = datetime.datetime.strptime(t, '%d %B %Y hour %H:%M:%S') 
# std = Student(id=None, student_number="106", name="binefş",surname="şimşek", birth_date=dt, gender="K", classid=2)
# db.add_student(std)




# year = input("yıl: ") or student[0].birth_date.year
# month = input("ay: ") or student[0].birth_date.month
# day = input("gün: ") or student[0].birth_date.day

# student[0].birth_date = datetime.date(year,month,day)

######### update TEST
# t = '13 October 2022 hour 20:42:18'
# dt = datetime.datetime.strptime(t, '%d %B %Y hour %H:%M:%S') 
# std = Student(id=3, student_number="500", name="KENDAL",surname="ŞİMŞEK", birth_date=dt, gender="K", classid=2)
# db.edit_student(std)


######### ders TEST
# result = db.getClasses()
# print(result[0].name)

