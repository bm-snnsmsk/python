kilo = float(input("Kilonuz : "))
boy = float(input("Boyunuz (1.80) : "))

index = kilo / (boy ** 2)

zayif = index >= 0 and index <= 18.4
normal = index >= 18.4 and index <= 24.9
kilolu = index >= 24.9 and index <= 29.9
obez = index >= 29.9 and index <= 34.9

if zayif :
    print(f"Zayıfsınız : {index}")
elif normal :
    print(f"Normal : {index}")
elif kilolu :
    print(f"kilolu : {index}")
elif obez :
    print(f"Obez : {index}")
else :
    print("Girilen bilgiler yanlış")
