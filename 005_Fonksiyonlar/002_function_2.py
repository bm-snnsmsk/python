print("value değerler".center(50,"*"))
def changename(n) :
    n = "ada"

name = "yiğit"

changename(name)
print(name)

print("references değerler".center(50,"*"))
########################################################################
def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"]

change(sehirler)
print(sehirler)


print("arguman = parameter".center(50,"*"))
########################################################################
def add(a,b):
    return sum((a,b))

def add2(*params):  ## parametreler tuple olduğunda *
    return sum((params))

def add3(*params):   # yukardaki ile aynı
    print(type(params))
    s = 0 
    for i in params :
        s = s + i
    return s

print(add(20,30))
# print(add(20,30,50))   ## hata verecek. 
print("arguman > parameter tuple değerler".center(50,"*"))
print(add2(20,30,40,50,60))
print(add3(20,30,40,50,60))


########################################################################
def displayUser(**args):  # parameterler dicitonary olduğunda **
    print(type(args))
    for key, value in args.items():
        print("{} is {} ".format(key,value))

print("arguman = parameter dicionary".center(50,"*"))
displayUser(name="çınar", age=2, city="istanbul")
displayUser(name="ada", age=12, city="mardin",telefon="1234")
displayUser(name="baran", age=3, city="mardin", telefon="12345",email="brn@gmail.com")


print("karışık".center(50,"*"))
########################################################################
def myfunc(a, b, *args, **kwargs) :
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(30,40,50,20,30,50,key1="val1", key2="val2")