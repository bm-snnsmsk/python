class Person :
    # class attributes
    address = "no information"

    # constructor (yapıcı metot)
    def __init__(self, name, year) :  # class'tan türetilen objeleri temsil eder
        # object attributes
        self.name = name
        self.year = year
        print("contructor metodu olan __init__ metodu otomatik çalıştı")

    # methods (instance metod o yüzden mutlaka self parametresi olmalı)
    def intro(self):
        print("hello python, ", self.name)

    def calculateAge(self) :
        return 2024 - self.year


# object (instance)
p1 = Person("sinan",1985)
p1.intro()
print(f"{p1.name}'ın yaşı : {p1.calculateAge()}")
print(dir(Person)
print(dir(Person.intro)

import math
class Circle :
    # class object attributes
    pi = math.pi

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    def cevre_hesapla(self) :
        return 2 * self.pi* self.yaricap

    def alan_hesapla(self) :
        return self.pi* self.yaricap ** 2
    

daire = Circle()
daire1 = Circle(5)

print(daire.cevre_hesapla())
print(daire.alan_hesapla())

print(daire1.cevre_hesapla())
print(daire1.alan_hesapla())

