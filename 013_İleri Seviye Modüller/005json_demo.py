import json
import os


class User :
    def __init__(self, username, password, email):
        ## validation kontrolleri burda yapılabilir
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self) :
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}   # giriş yapan kullanıcı bilgileri

        # load users from .json File
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                # print(users)  # test
                for user in users:
                    user = json.loads(user) # sölük
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu...")

    def login(self, username, password):
        for i in self.users:
            if username == username and password == password :
                self.isLoggedIn = True
                self.currentUser = i
                print(f"Giriş başarılı {i.username}")
                break
            else:
                print("Böyle bir kullanıcı yok")
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giriş yapılmadı.')

    def savetoFile(self):
        # json class objeyi almadığı için öncelikle class objeyi dict'e çeviriyoruz
        liste = []
        for i in self.users :        
            liste.append(json.dumps(i.__dict__))

        with open("users.json", "w") as f :
            # json.dump(self.users, f) ## users objesi almaz
            json.dump(liste, f)


repository = UserRepository()

while True :
    print("Menü".center(50,"*"))
    secim = input('1 - Register\n2 - Login\n3 - Logout\n4 - İdentity\n5 - Çıkış\nSeçiminiz : ')
    if secim == '5' :
        break
    else : 
        if secim == '1' :
            username = input("Username : ")
            password = input("Şifreniz : ")
            email = input("Email : ")
            user = User(username, password, email)
            repository.register(user)

            # print(repository.users)


        elif secim == '2' :
            if repository.isLoggedIn:
                print('zaten login oldunuz')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)

        elif secim == '3' :
            repository.logout()

        elif secim == '4' :
            repository.identity()

        else :
            print("Yanlış seçim!")
         