# days = int(input("Aracınız kaç gündür trafiktedir?"))

# if days <= 365 :
#     print("1. servis yılı aralığı")
# elif days > 365 and days <= 365*2 :
#     print("2. servis yılı aralığı")

# elif days > 365*2 and days <= 365*3 :
#     print("3. servis yılı aralığı")
# else :
#     print("Hatalı giriş")



import datetime

tarih = input("Aracınız kaç gündür trafiktedir (2009/11/23)?")
tarih = tarih.split("/")
print(tarih[0])
print(tarih[1])
print(tarih[2])

trafige_cikis_tarihi = datetime.datetime(int(tarih[0]), int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafige_cikis_tarihi

print(fark.days)

if fark.days <= 365 :
    print("1. servis yılı aralığı")
elif fark.days > 365 and fark.days <= 365*2 :
    print("2. servis yılı aralığı")

elif fark.days > 365*2 and fark.days <= 365*3 :
    print("3. servis yılı aralığı")
else :
    print("Hatalı giriş")

