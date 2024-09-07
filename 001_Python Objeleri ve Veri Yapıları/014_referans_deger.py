# value types => strings, number
x = 5
y = 25

x = y
y = 10

print(x)
print(y)


# referanse types => list, class

a = ["apple","banana"]
b = ["apple","banana"]

a = b
b[0] = "grape"  # sadece b listesinde değişiklik yapılmasına rağmen her iki liste de değişir.Çünkü Value type'lerde değer tutulur, listelerde ise address bilgisi tutulur addreler ise başka bir yerdeki değerleri işaret eder. Yani değerler eğitlendiğinde değerler değil adresler birbirne eşit olur ve bu adreslerde tutulan değerler değişince her iki liste de değişmiş olur. Amaç performans

# a[0] = "çilek"

print(a,b)