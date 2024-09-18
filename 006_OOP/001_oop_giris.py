#class
# instance = class koypyası

'''
class Person :
    class attributes
    object attributes

    methods
    
class Person(isim) :
    name = isim
    def metot(self):
        self.name = "kisi"
        
    class attributes
    object attributes

    methods




object, instance
obje1 = Person()
obje1.attr
'''

'''
Person                      let sinan
name                        sinan
yearOfBirth                 1985       age = sinan.calculateAge()
job                         computer engineer
calculateAge()

class                       instance (obje)

'''

class Deneme :
    pass

class Person :
    # class attributes
    address = "no information"

    # constructor (yapıcı metot)
    def __init__(self, name, year) :  # class'tan türetilen objeleri temsil eder
        # object attributes
        self.name = name
        self.year = year
        print("contructor metodu olan __init__ metodu otomatik çalıştı")


    # methods


# object (instance)
p1 = Person("sinan",1985)
p2 = Person(year=2021, name="baran")

print(p1)
print(type(p1))
print(p2)
print(type(p2))


# accessing object attributes
print(f"p1 objesi isim : {p1.name}, doğum yılı : {p1.year}, adresi : {p1.address}")
print(f"p2 objesi isim : {p2.name}, doğum yılı : {p2.year}")

# updating
p1.name = "emine"
p1.address = "mardin"
print(f"p1 objesi isim : {p1.name}, doğum yılı : {p1.year}, adresi : {p1.address}")
