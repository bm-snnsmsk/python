# inheritance kalıtım

# class Person :   
#     def __init__(self) :  
#         print("Person created")

# class Student(Person) :
#     def __init__(self) :  
#         Person.__init__(self) # amaç Person clasındaki contructor attributeslerine erişebilmek
#         print("Student created")


class Person :   
    def __init__(self, isim, soyisim) :  
        self.isim = isim
        self.soyisim = soyisim
        print("Person created")

    def who_am_i(self):
        print("ben bir kişiyim")

    def sayHello(self):
        print("selamlar")

class Student(Person) :
    def __init__(self, i, s, numara) :  
        Person.__init__(self, i, s) # amaç Person clasındaki contructor attributeslerine erişebilmek
        self.ogrno = numara
        print(f"{self.ogrno} numaralı bir Student created")

    # override
    def who_am_i(self):  
        print("ben bir öğrenciyim")


class Teacher(Person) :
    def __init__(self, isim, surname, brans) :
        # Person.__init__(self, isim, surname) # veya
        super().__init__(isim, surname)  ## super'da self'e gerek yok
        self.branch = brans
        
    
    # override
    def who_am_i(self):
        print(f"ben {self.branch} öğretmeniyim")


# s1 = Student()

# s1 = Student("tuba", "şimşek", 201)
# print(f"{s1.isim}, {s1.soyisim}, {s1.ogrno}")
# s1.who_am_i()

ogretmen1 = Teacher("zozan","şimşek", "anaokul")
print(ogretmen1.isim, ogretmen1.branch)
ogretmen1.who_am_i()