# encapsülation


def fact(number) :

    # encapsülation 
    if not isinstance(num, int):
        raise TypeError("number must be an integer")
    if not number > 0 :
        raise ValueError("sayı 0'dan büyük olmalı")
    # encapsülation 
    
    def inner(number):
        if number <= 1 :
            return 1
        return number * inner(number - 1)
    return inner(number)

try:
    # print(fact("s"))
    # print(fact(-4))
    print(fact(0))
    print(fact(5))
except Exception as err :
    print(err)