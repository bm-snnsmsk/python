from db_connection import conn
import datetime
import time

class Student :
    conn = conn #gerek varmıydı ??? evet
    curs = conn.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender) :
        if id is None :
            self.id = 0
        else :
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self) :
        # sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        sql = "INSERT INTO student (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        # self.curs.execute(sql, value)
        Student.curs.execute(sql, value)        

        try : 
            Student.conn.commit()
            print(f"{self.curs.rowcount} tane kayıt eklendi")
        except Exception as err :
            print(f"Hata : {err}")
        finally : 
            self.conn.close()

    @staticmethod  ## bu kodla ağaşıda self kullanmaya gerek yok, ayrıca instance tanımlanmadan bu bu method class ismiyle kullanılabilir.
    def saveStudents(datas) :
        # sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        sql = "INSERT INTO student (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        values = datas
        Student.curs.executemany(sql, values)        

        try : 
            Student.conn.commit()
            print(f"{Student.curs.rowcount} tane kayıt eklendi")
        except Exception as err :
            print(f"Hata : {err}")
        finally : 
            Student.conn.close()


    @staticmethod 
    def getStudents() :
        sql = "SELECT * FROM student LIMIT 10"
        sql = "SELECT StudentNumber, name, surname FROM student"
        sql = "SELECT name, surname FROM student WHERE gender = 'K' "
        sql = "SELECT * FROM student WHERE YEAR(birthdate) = 2003"
        sql = "SELECT * FROM student WHERE name = 'ali' and YEAR(birthdate) = 2005"
        sql = "SELECT * FROM student WHERE name LIKE '%an%' or surname LIKE '%an%'"
        kac_kisi = "SELECT COUNT(*) FROM student WHERE gender = 'E'"
        sql = "SELECT * FROM student WHERE gender='K' ORDER BY name, surname"



        Student.curs.execute(sql)      
        # Student.curs.execute(kac_kisi)      

        try : 
            result = Student.curs.fetchall()
            for i in result : 
                # print(i[2])
                print(i)

            # result = Student.curs.fetchone()
            # print(result)

        except Exception as err :
            print(f"Hata : {err}")
        finally : 
            Student.conn.close()

    @staticmethod
    def getStudentById(id) :
        sql = "SELECT * FROM student WHERE id=%s"
        value = (id,)
        Student.curs.execute(sql, value)        

        try : 
           return Student.curs.fetchone()
        except Exception as err :
            print(f"Hata : {err}")
      

    
    def updateStudent(self) :
        sql = "UPDATE student SET name = %s, surname=%s WHERE id=%s"
        value = (self.name, self.surname, self.id)
        Student.curs.execute(sql, value)        

        try : 
            Student.conn.commit()
            print(f"{Student.curs.rowcount} tane kayıt güncellendi")
        except Exception as err :
            print(f"Hata : {err}")

    @staticmethod
    def updateStudents(liste) :
        sql = "UPDATE student SET name = %s, surname=%s WHERE id=%s"
        value = liste
        Student.curs.executemany(sql, value)        

        try : 
            Student.conn.commit()
            print(f"{Student.curs.rowcount} tane kayıt güncellendi")
        except Exception as err :
            print(f"Hata : {err}")

    
    
    @staticmethod
    def getStudentsGender(gender) :
        sql = "SELECT * FROM student WHERE gender=%s"
        values = (gender,)
        Student.curs.execute(sql, values)        

        try : 
           return Student.curs.fetchall()
        except Exception as err :
            print(f"Hata : {err}")
      




ogrenci_listesi = [
    ("115","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"),
    ("116","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"),
    ("117","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"),
    ("118","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"),
    ("119","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"),
    ("120","ahmet","yılmaz",datetime.datetime(2003, 5, 17), "E"),
]


# ogrenci_1 = Student("114","bahar","beniaffet",datetime.datetime(2000, 7, 27), "K")
# ogrenci_1.saveStudents(ogrenci_listesi)

Student.saveStudents(ogrenci_listesi)
# Student.getStudents()

# stu = Student.getStudentById(23)
# print(stu)
# print(stu)

# student = Student(stu[0], stu[1], stu[2], stu[3], stu[4], stu[5])
# student.name = "sinan"
# student.surname = "şimşek"
# student.updateStudent()

# student = Student.getStudentsGender("K")
# for i in student :
#     print(i)

# liste = [
#     ("sinan", "şimşek", 20),
#     ("tuba", "şimşek", 21),
#     ("emine", "şimşek", 22),
# ]

# Student.updateStudents(liste)
