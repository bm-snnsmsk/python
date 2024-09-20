import numpy as np


result = np.random.randint(10,50,15).reshape(3,5)
matris = np.random.randint(-50,50,15).reshape(3,5)

result = matris ** 2

ciftler = matris[matris % 2 == 0]
result = ciftler[ciftler>0]


print(matris)
print(result)