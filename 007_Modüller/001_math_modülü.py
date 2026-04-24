# 1 - kendi hazırladığımız modüller
# 2 - hazır modüller
# 2a - Standart kütühane modülleri
# 2b - 3. şahıs modülleri   (pypi.org)  >>> pip install paket_adi

# import math 

# print(dir(math))    ### math modülündeki metotlar
# print(help(math))
# print(help(math.pow))   ### metot hakkındaki açıklama


import math as islem 
print(islem.factorial(5))
print(islem.sqrt(5))
print(islem.pow(5,3))


## alternatif kullanım
from math import *
from math import factorial, floor

def sqrt(x) :
    print(f"x : {x}")
sqrt(5)  ## en son yazılan metot geçerli

###############################################################################
import math

## ebob
print(math.gcd(39, 65))



## built-in fonksiyonlar   ###  metot class fonksiyonlarıdır
print(bin(65))
print(hex(65))
print(chr(65))
print(oct(65))


liste = [1,2,3,4,5]
print(sum(liste))



