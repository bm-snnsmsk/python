def yetki_sorgu(page):
    def inner(role):
        if role == "admin" :
            return f"{role} rolü {page} sayfasına ulaşabilir." 
        else :
            return f"{role} rolü {page} sayfasına ulaşamaz.. " 
    return inner

user1 = yetki_sorgu("Product Edit")
print(user1("admin"))
print(user1("user"))

#####################################################################

def islem(islem_adi) :
    def toplama(*args) :
        toplam = 0
        for i in args :
            toplam += i
        return toplam
    
    def carpma(*args) :
        carpim = 1
        for i in args :
            carpim *= i
        return carpim
    
    if islem_adi == "toplama" :
        return toplama
    elif islem_adi == "carpma" :
        return carpma
    

islem1 = islem("toplama")
print(islem1(6,8,4,5,9))

islem2 = islem("carpma")
print(islem2(6,8,4,5,9))