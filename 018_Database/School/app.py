from db_manager import DbManager
from student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent() 
            elif islem == '4':
                self.deleteStudent() 
            elif islem == 'E' or islem =='Ç':
                break
            else:
                print('yanlış seçim')


    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('öğrenci id: '))

        self.db.delete_student(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('öğrenci id: '))

        student = self.db.get_student_by_id(studentid)

        student[0].name = input('name:') or student[0].name
        student[0].surname = input('surname:') or student[0].surname
        student[0].gender = input('cinsiyet (E/K):') or student[0].gender
        student[0].classid = input('sınıf: ') or student[0].classid

        year = int(input("yıl: ")) or student[0].birth_date.year
        month = int(input("ay: ")) or student[0].birth_date.month
        day = int(input("gün: ")) or student[0].birth_date.day

        student[0].birth_date = datetime.date(year,month,day)
        self.db.edit_student(student[0]) 

    def addStudent(self):
        self.displayClasses()
        
        classid = int(input('hangi sınıf: '))
        number = input('numara: ')
        name = input('ad')
        surname = input('soyad')
        year = int(input('yıl'))
        month = int(input('ay'))
        day = int(input('gün'))
        birthdate = datetime.date(year,month,day)
        gender = input('cinsiyet (E/K)')

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.add_student(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):       
        self.displayClasses()
        classid = int(input('hangi sınıf: '))

        students = self.db.get_students_by_class_id(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid

    



app = App()     
app.initApp()