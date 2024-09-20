import numpy as np

result = np.array([1,3,5,7,9,11])
result = np.arange(1,10)  ## 1 den 10' a kadar
result = np.arange(10,100, 3) # 10 dan 100' e akdar 3 atlayarak
result = np.zeros(10) ## 10  sıfır float 
result = np.ones(10)  ## 10 bir float
result = np.linspace(0, 100, 5)  ## aralığı 5 e böl
result = np.linspace(0, 100, 5)  ## aralığı 5 e böl
result = np.random.randint(0, 10)  ## 0-10 aralığında rastgele bir sayı
result = np.random.randint(0, 10, 3)  ## 0-10 aralığında rastgele 3 sayı
result = np.random.rand(5)  ## 0-1 aralığında rastgele 5 sayı
result = np.random.randn(5)  ## 0-1 aralığında rastgele 5 negatif sayı
result = np.random.randn(5)  ## 0-1 aralığında rastgele 5 negatif sayı

# print(result)

np_array = np.arange(50)
np_multi = np_array.reshape(5, 10) # 5 satır 10 sütun

print(np_multi)
print(np_multi.sum(axis=1))  ## her satırdaki sayıların tıoplamı
print(np_multi.sum(axis=0))  ## her sutundaki sayıların tıoplamı

rand_numbers = np.random.randint(1, 100, 10)
result = rand_numbers.max()
result = rand_numbers.min()
result = rand_numbers.mean()  # ortalama
result = rand_numbers.argmax()  # max sayının indexi
result = rand_numbers.argmin()  # min sayının indexi

print(rand_numbers)
print(result)