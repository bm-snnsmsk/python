###############################################################
# liste = ["1","2ö","32","lk","54"]
# for i in liste :
#     try :
#         print(int(i))
#     except Exception :
#         continue
###############################################################
# while True :
#     sayi = input("sayi : ")
#     if sayi == "q".lower() :
#         break
#     try :        
#         print(float(sayi))
#         break
#     except Exception :
#         print("geçersiz değer")
#         continue
###############################################################
# def check_parola(parola) :
#     turkce_karakterler = "çÇğĞıİöÖşŞüÜ"
#     for i in parola :
#         if i in turkce_karakterler :
#             raise TypeError("parola türkçe karakter içeremez")
#         else :
#             pass
#     print("geçerli parola")

# parola = input("parola giriniz : ")
# try :
#     check_parola(parola)
# except Exception as err:
#     print(err)
###############################################################
def factoriyel(x) :
    x = int(x)
    if x < 0 :
        raise ValueError("negatif değer")
    result = 1
    for i in range(1, x + 1) :
        result *= i
    
    return result

for i in [5, 10, 20, -3, "10a"] :
    try :
        y = factoriyel(i)
    except Exception as err :
        print(err)
        continue
    print(y)

###############################################################
