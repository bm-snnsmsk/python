class Student :
    def __init__(self, id, student_number, name, surname, birth_date, gender, classid) :
        if id is None :
            self.id = 0
        else :
            self.id = id
        self.student_number = student_number
        if len(name) > 45 :
            raise Exception("isim max 45 karakter olmalı")
        self.name = name
        self.surname = surname
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.classid = classid
    
    @staticmethod
    def CreateStudent(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list
