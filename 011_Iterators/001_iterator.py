liste = [1,2,3,4,5]

## for döngüsü bu işlemi zaten yapıyor
iterator = iter(liste)
# print(dir(iterator))
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))   ## altıncısı stop iteration hatası verecektir


# for döngüsünün yaptığı
# while True :
#     try :
#         element = next(iterator)
#         print(element)
#     except StopIteration :
#         break


class MyNumbers:
    def __init__(self, start, stop) :
        self.start = start
        self.stop = stop

    def __iter__(self) :
        return self
    
    def __next__(self) :
        if self.start <= self.stop :
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
sonuc = MyNumbers(3, 17)
for i in sonuc :
    print(i)
