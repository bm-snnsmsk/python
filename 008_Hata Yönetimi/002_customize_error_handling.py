###############################################################
# x = 10 
# if x >= 5 :
#     raise Exception("x 5 ten büyük olamaz")
###############################################################
def check_password(psw) :
    import re
    if len(psw) < 8 :
        raise Exception("parola en az 7 karakter olmalı")
    elif not re.search("[a-z]", psw) :
        raise Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]", psw) :
        raise Exception("parola büyük harf içermeli")
    elif not re.search("[0-9]", psw) :
        raise Exception("parola rakam içermeli")
    elif not re.search("[_@$]", psw) :
        raise Exception("parola alfa numeric karakter içermeli")
    elif re.search("[\s]", psw) :
        raise Exception("parola boşluk içermemeli")
    else :
        print("geçerli parola")

password = "1254qqA22"

try : 
    check_password(password)
except Exception as e :
    print(e)
else :
    print("herşey yolunda")
finally :
    print("finally her zaman çalışır")
###############################################################

class Person :
    def __init__(self, name, year) :
        if len(name) > 10 :
            raise Exception("isim alanı 10 karakterden büyük olmalmalı")
        else : 
            name = name

person = Person("Sinan şimşek", 1989)   >>>> hatayı sşöyle fırlatır
### # Traceback (most recent call last):
#   File "c:\Users\bm_snnsmsk\Desktop\python\010\02.py", line 39, in <module>
#     person = Person("Sinan şimşek", 1989)
#   File "c:\Users\bm_snnsmsk\Desktop\python\010\02.py", line 35, in __init__
#     raise Exception("isim alanı 10 karakterden büyük olmalmalı")
# Exception: isim alanı 10 karakterden büyük olmalmalı
        
