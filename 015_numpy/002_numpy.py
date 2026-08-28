import numpy as np

result = np.array([1,3,5,7,9,11])
result = np.array([1,3,5,7,9,11]).reshape(3,2)   ### eleman sayısı sutun X satır sçarpımını karşılamalı
result = np.arange(1,10)  ## 1 den başla 10' a kadar
result = np.arange(1,10).reshape(3,3)   ### eleman sayısı sutun X satır sçarpımını karşılamalı  ## 1 den başla 10' a kadar
result = np.arange(10,100, 3) # 10 dan başla 100' e akdar 3 atlayarak
result = np.zeros(10).reshape(5,2)   ### eleman sayısı sutun X satır sçarpımını karşılamalı ## 10  sıfır float 
result = np.ones(10)  ## 10 bir float
result = np.linspace(0, 100, 5)  ## 0-100 aralığında eşit aralıklı 5 tane sayı >>> [  0.  25.  50.  75. 100.]
result = np.linspace(0, 5, 8)  ## [0.  0.71428571 1.42857143 2.14285714 2.85714286 3.57142857 4.28571429 5. ]   >>> 0-5 aralığında eşit aralıklı 8 tane sayı 


result = np.random.randint(0, 10)  ## 0-10 aralığında rastgele bir sayı

result = np.random.randint(0, 5, 1000)  ## 0-5 aralığında rastgele 1000 sayı
liste = []
for i in range(10000) :
    liste.append(np.random.randint(0, 5))
print(liste.count(0))
print(liste.count(1))
print(liste.count(2))
print(liste.count(3))
print(liste.count(4))
print(liste.count(5))

print(liste) >>>> [1, 3, 3, 1, 0, 4, 3, 3, 3, 1, 1, 2, 1, 0, 0, 2, 4, 3, 4, 3, 3, 1, 2, 3, 4, 4, 2, 4, 3, 0, 1, 1, 1, 3, 3, 1, 1, 0, 3, 2, 4, 4, 4, 3, 1, 3, 4, 3, 4, 4, 1, 3, 0, 2, 2, 0, 3, 0, 3, 4, 1, 1, 0, 0, 0, 0, 3, 2, 2, 1, 3, 3, 3, 1, 2, 0, 1, 4, 0, 0, 4, 2, 1, 4, 0, 2, 3, 3, 4, 1, 2, 2, 0, 3, 1, 0, 3, 0, 4, 3]
print(result) >>> [2 4 2 0 0 1 0 4 0 3 4 0 4 0 3 4 3 4 3 0 0 2 4 0 0 2 1 0 2 3 3 1 4 4 0 2 2
 0 3 3 3 4 4 1 0 2 3 0 0 0 0 1 4 3 4 1 0 0 0 2 0 2 0 2 3 4 1 3 2 1 2 0 4 3
 4 4 3 0 2 1 4 4 2 3 3 2 2 3 4 3 4 4 3 3 4 3 0 3 0 0]

result = np.random.rand(5)  ## 0-1 aralığında rastgele 5 sayı
result = np.random.randn(5)  ## 0-1 aralığında rastgele 5 tane porizitif veya negatif sayı >>> [-0.70195693  1.06071423  1.82678196 -1.84203482 -0.27114043]


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
