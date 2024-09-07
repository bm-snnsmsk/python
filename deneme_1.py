# kucuk = 10
# buyuk = 17
# asalmi = True
# asal = []

# for i in range(kucuk, buyuk + 1):
#     for j in range(2, i):
#         if i % j == 0 :
#             asalmi = False
#             break    
#     if asalmi  :
#         asal.append(i)

# print(asal)



# for i in range(0,10):
#     for j in range(0, i) :
#         print("*")
#     print("\n")


s1 = 7
s2 = 11
asalsayilar = []

for i in range(s1, s2+1):
    isAsal = True
    for j in range(2, i) :
        if i % j == 0 :
            print(f"{i} {j}'yi tam bölüyor. Bu yüzden {i} sayısı asal değildir")
            isAsal = False
            break
    if isAsal :
        asalsayilar.append(i)
        
    
print(asalsayilar)