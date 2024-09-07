username = "snn"
password = "1234"
isLoggedin = (username == "snn") and (password == "1234")

if isLoggedin : 
    print(f"Giriş başarılı. Hoş geldiniz {username}")
else :
    print("Yetkisiz giriş")



x = 40
y = 30 

if x > y :
    print(f"{x}, {y}'den büyüktür.")
elif x < y :
    print(f"{x}, {y}'den küçüktür.")
else :
    print(f"{x}, {y}'e eşittir.")