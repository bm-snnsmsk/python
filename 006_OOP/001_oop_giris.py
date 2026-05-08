#class
# instance = class koypyası

'''
class Person :
    class attributes
    object attributes

    methods(self parametresi zorunlu)
    
class Person :
    pass
    
class Person() :
    pass
    
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

class CartItem:

    ## 
    discount_rate2 = 0.8
    item_count2 = 0



    # constructor => yapıcı metot
    def __init__(self, name, price, quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."

    # instance methods
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self, rate):
        self.price = self.price * rate
        ## self.price = self.price * CartItem.discount_rate

# instance => nesne, örnek
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
item3 = CartItem("kitap", 200, 2)

item1.apply_discount(0.8)
print(item1.calculate_total())

item2.apply_discount(0.7)
print(item2.calculate_total())

item3.apply_discount(0.9)
print(item3.calculate_total())


#############################################

def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    #### 2. yöntem # print(p.name, p.price) çağrılmak için
    @property
    def price(self):
        return self._price
    
    @price.setter  # print(p.name, p.price) çağrılmak için
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
        ### 1. yöntem    
    # def set_price(self, value):
    #     if value >= 0:
    #         self._price = value
    #     else:
    #         raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    # def get_price(self):
    #     return self._price

    
###################################################

class Deneme :
    pass

class Person :
    # class attributes
    address = "no information"

    # constructor (yapıcı metot) # return kullanılmaz
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
