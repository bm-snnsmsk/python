import math, time

def usalma(a, b) :
    start = time.time()
    time.sleep(1)
    print(math.pow(a,b))
    finish = time.time()
    print("fonksiyon "+str(finish - start)+" sn sürdü")

def factoriyel(a) :
    start = time.time()
    time.sleep(1)
    print(math.factorial(a))
    finish = time.time()
    print("fonksiyon "+str(finish - start)+" sn sürdü")



usalma(2,3)
factoriyel(5)

## yukrdaki den daha sade dah kullanışlı
def calculate_time(func) :
    def inner(*args, **kwargs) :
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("fonksiyon ("+func.__name__+ ") "+str(finish - start)+" sn sürdü")
    return inner

@calculate_time
def usalma2(a, b) :
    print(math.pow(a,b))

@calculate_time
def factoriyel2(a) :
    print(math.factorial(a))

usalma2(3,3)
factoriyel2(6)