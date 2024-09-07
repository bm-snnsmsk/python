def kontrol(deger) : return deger % 2 == 0

liste = [1, 10, 3, 5, 22, 12, 9]

print(list(map(kontrol, liste)))  # true false olarak döner
print(list(filter(kontrol, liste)))  # şartı sağlayan olanlar döner


print("".center(50,"*"))
print(liste)
check = lambda sayi : sayi % 2 == 0
print(list(map(check, liste)))
print(list(filter(check, liste)))