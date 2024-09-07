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

for i in range(s1, s2):
    print("i değeri : ",i)
    for j in range(2, i) :
        print("j değeri : ",j)
        if i % j == 0 :
            print(f"{i} {j} tam bölen")
        else : 
            print(f"{i} {j} tam bölüğnmüyor :")