mesaj = "hello there. my name is sinan".split()
result1 = type(mesaj)

my_list = [1, 2 , 3, 4, 5]
my_list2 = ["bir", 2 , True, 4.5]

isim = "sinan"
print(isim)
to_list = list(isim)
print(to_list)


result2 = my_list + my_list2
result22 = my_list.extend(my_list2) # = my_list + my_list2 #  my_list2 aynı ama my_list artık değişmiştir
result3 = len(my_list)
result4 = my_list2[0]
result5 = [my_list + my_list2]   # tek elemanlı bir liste
result6 = [my_list, my_list2]     # çift elemanlı bir liste

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result5[0][1])
# print(result6[0][1])

arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]

result7 = len(arabalar)


print(result7)
print(arabalar[0])
print(arabalar[-1])
arabalar[-1] = "Toyota"
print(arabalar)
print(arabalar[-2])
print("Mercedes" in arabalar)
print(arabalar[:3])   ## ilk 3 elemaqn
print(arabalar[-2:])  
arabalar[-2:] = ["tofaş", "golf"]
print(arabalar)
result8 = arabalar + ["caddy","ford"]
print(result8)   

del arabalar[-1]   ## son elemanı sil
print(arabalar)
print(arabalar[::-1])


