# print(x)          => NameError
# int("1a2")        => ValueError
# print(10/0)       => ZeroDivisionError
# print("denem"e)   => SyntaxError

# Error

# Error Handling     =>  Hata Yönetimi

# try :
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)
# except ZeroDivisionError :  ## except (ZeroDivisionError, ValueError) :
#     print("y 0 olamaz")
# except ValueError :
#     print("x ve y sayısal değerler olmalı")


# try :
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e: 
#     print("yanlış bilgi")
#     print(e)

# try :
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)
# except : 
#     print("yanlış bilgi")
# else: 
#     print("herşey yolunda")


# while True :  # doğru bilgi girilene kadar userdan bilgi alır
#     try :
#         x = int(input("x : "))
#         y = int(input("y : "))
#         print(x/y)
#     except : 
#         print("yanlış bilgi")
#     else: 
#         break



try :
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except Exception as e: 
    print("yanlış bilgi")
    print(e)
else: 
    print("herşey yolunda")
finally :
    print("hata olsa da olmasa da çalışan blok")
    ## dosya açma kapatma gibi projelerde kullanılıır
    ## veya database kapatma

