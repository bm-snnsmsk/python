import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])
result = numbers[5] # 5. index
result = numbers[-1] # son index
result = numbers[0:3] #ilk 3 değer
result = numbers[:3] #ilk 3 değer
result = numbers[3:] # 3. indexten sonraki
result = numbers[::] # baştan birer birer sırala
result = numbers[::-1] # sondan sırala
result = numbers[::-2] # sondan sırala 2er olarak

numbers2 = np.array([[0,5,10], [15,20,25], [50,75,85]])

result = numbers2[0] # [0,5,10]
result = numbers2[0][2] # 10
result = numbers2[0,2] # 10
result = numbers2[2, 1] # 75
result = numbers2[:, 2] # tüm satırların 2. indexleri
result = numbers2[:, 0] # tüm satırların 0. indexleri
result = numbers2[:, 0:2] # tüm satırların 0. - 2. index aralığı
result = numbers2[-1, :] # son satırın tüm elemanları 
result = numbers2[:3, :3] # tüm satırların tüm elemanları 

# print(result)

arr1 = np.arange(0,10)
arr2 = arr1  ## referans 
arr3 = arr1.copy()  ## değer  
arr2[3] = 20 # her iki dizinin ilgili indexi değişri
arr3[0] = 100
print(arr1)
print(arr2)
print(arr3)

