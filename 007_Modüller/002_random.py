import random 

# print(dir(random))
# print(help(random))
# print(help(random.shuffle))

print(random.random())  # 0.0 - 1.0
print(random.uniform(3,5))  # 3.0 - 4.999
print(random.randint(3,50))  # 3 - 50
liste = ["sinan","baran","tuba","emine"]
print(random.randint(0, len(liste) - 1))
print(random.choice(liste))
print(liste)
random.shuffle(liste)
print(liste)

print(random.sample(range(100), 4))  ## listeden belirli sayıda eleman almak
print(random.sample(liste, 2))  ## listeden belirli sayıda eleman almak

print(random.randrange(1,13,2)  ## 1, 13 aralığında 2şer atlayarak sayı üret. Tek sayılar


