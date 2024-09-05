name = "sinan"
surname = "şimşek"
age = 39

# selamlama = "benim adım "+ name + " " + surname +" ve " + str(age) + " yaşındayım"




print("benim adım {}".format(name))
print("benim adım {} {}".format(name, surname))
print("benim adım {1} {0}".format(name, surname))
print("benim adım {a} {s} {n}".format(n=name, s=surname, a=age))

print(f"benim adım {name} {age} {surname}")

result = 200 / 700
print("sonuc : {r}".format(r=result))
print("sonuc : {r:1.3}".format(r=result))   # 0.286
print(f"sonuc : {result:1.3}")   # 0.286
