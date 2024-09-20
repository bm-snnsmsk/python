## numpy daha çok sayılar
## pandas daha çok data setleri
## kaggle.com/datasets
## https://pandas.pydata.org/

import pandas as pd
import numpy as np


# pandas_series = pd.Series()
numbers = [10,20,30,40,50]
# letters = ["10","20","30","40","50"]
# mix = ["10",40,300,"40","50"]
# scaler = 20
# dict = {"a":10,"b":20,"c":30,"d":40}

# print(pandas_series) # Series([], dtype: object)
# print(pd.Series(numbers)) # dtype: int64
# print(pd.Series(mix)) #dtype: object
# print(pd.Series(letters)) # dtype: object
# print(pd.Series(scaler)) # dtype: int64
# print(pd.Series(5, [0,1,2,3,4])) # 0    51    52    53    54    5dtype:int64
# print(pd.Series(numbers, ["a","b","c","d","e"])) # sıra numarası harfler ile gösterilir
# print(pd.Series(dict))

# random_numbers = random_numbers = np.random.randint(10,100,6)
# pandas_series = pd.Series(random_numbers)
# print(pandas_series)

pandas_series = pd.Series(numbers, ['a','b','c','d', 'e'])

# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series['a']
# result = pandas_series['d']
# result = pandas_series[['a','c','e', 'f']] ## hata vermez NaN değeri verir
# result = pandas_series.ndim
# result = pandas_series.dtype
# result = pandas_series.shape
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.min()
# result = pandas_series + pandas_series
# result = pandas_series + 50
# result = np.sqrt(pandas_series)

# result = pandas_series >=50
# result = pandas_series % 2 == 0

# print(pandas_series)
# print(result)

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

total = opel2018 + opel2019
print(total)
# print(total["astra"])