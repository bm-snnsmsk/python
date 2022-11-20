class User :
    pass

class UserRepository :
    def register(self) :
        pass
    def login(self) :
        pass
    def savetoFile(self) :
        pass


while True :
    print("Menü".center(50,"*")) 
    secim = input("1 - Register\n2 - Login\n3 - Logout\n4 - Identity\n5 - Exit\n\nSeçiminiz : ")
    if secim == "1" :
        #register
        pass
    elif secim == "2" :
        #login
        pass
    elif secim == "3" :
        #logout
        pass
    elif secim == "4" :
        #identity
        pass
    elif secim == "5" :
        break
    else :
        print("Yanlış seçim")
