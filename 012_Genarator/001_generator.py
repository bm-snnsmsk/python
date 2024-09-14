# bellek üzerinde yer tutan yapı
def cube() :
    result = []
    for i in range(5) :
        result.append(i**3)
    return result

print(cube())

# bir değer bir listede tutulmak gerke yoksa 
# bellek üzerinde yer tutmayan yapı
def cube() :
    for i in range(5) :
        yield i**3 # bu değerler talep edilir ve işlem durur  2. bir defa istense gösterilmez

generator = cube()
iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))

liste = [i**3 for i in range(5)]
generator_liste = (i**3 for i in range(5))
print(generator_liste)

print(next(generator_liste))
print(next(generator_liste))
print(next(generator_liste))