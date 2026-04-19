# value types => strings, number
# value tipler değer taşır

x = 5
y = 25

x = y
y = 10

print(x)
print(y)


# referanse types => list, class
## referans tipler adres taşır, o yüzeden adr4steki değişkilk o adresi referans alan tüm değerleri etiler

a = ["apple","banana"]
b = ["apple","banana"]

a = b   ### list, class veriler referans tipler olduğu için adresler eşitleinir
b[0] = "grape"  # sadece b listesinde değişiklik yapılmasına rağmen her iki liste de değişir.Çünkü Value type'lerde değer tutulur, listelerde ise address bilgisi tutulur addreler ise başka bir yerdeki değerleri işaret eder. Yani değerler eğitlendiğinde değerler değil adresler birbirne eşit olur ve bu adreslerde tutulan değerler değişince her iki liste de değişmiş olur. Amaç performans

# a[0] = "çilek"

print(a,b)
