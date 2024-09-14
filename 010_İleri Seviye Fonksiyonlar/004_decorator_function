def my_decorator(func) :
    def wrapper() :
        print("fonksiyondan önce")
        func()
        print("fonksiyondan sonra")
    return wrapper

def my_decorator2(func) :
    def wrapper(name) :
        print("fonksiyondan önce")
        func(name)
        print("fonksiyondan sonra")
    return wrapper


def sayHello():
    print("hello")

def selamlama():
    print("selamlar")

hello = my_decorator(sayHello)
selam = my_decorator(selamlama)
hello()
selam()

## yukardakilerin yerine 
@my_decorator
def merhaba() :
    print("merhabalar")

merhaba()

## yukardakilerin yerine 
@my_decorator2
def merhaba2(isim) :
    print("merhabalar", isim)


merhaba2("sinan")