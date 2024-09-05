name = "sinan"
surname = "şimşek"
age = 39

selamlama = "benim adım "+ name + " " + surname +" ve " + str(age) + " yaşındayım"

print(selamlama)
print(selamlama[0])
print(len(selamlama))
print(selamlama[-1])  # len(selamlama) - 1
print(selamlama[len(selamlama) - 1])

print(selamlama[2:5])
print(selamlama[2:])
print(selamlama[:21])
print(selamlama[2:30:2])   # ikişer ikişer al

demo = "baran"
print(demo[::1])
print(demo[::-1])

demo2 = "tuba" * 5
print(demo2)
print(demo2[::4])