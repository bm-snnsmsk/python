numbers = [1, 2, 3, 4, 5]

print("Liste".center(50,"*"))
for i in numbers :
    print(i)

tuple = [(1, 2), (1,3), (3,5), (5,7)]
print("tuple".center(50,"*"))
for i in tuple :
    print(i)

print("tuple".center(50,"*"))
for i,j in tuple :
    print(i)

print("tuple".center(50,"*"))
for i,j in tuple :
    print(i,j)

print("Dictionary 1".center(50,"*"))
d = {"k1":1,"k2":2,"k3":3}
for key in d :
    print(key)

d = {"k1":10,"k2":20,"k3":30}
print("Dictionary 2".center(50,"*"))
for key in d.items() :
    print(key)
print("Dictionary 3".center(50,"*"))
for key,val in d.items() :
    print(val)
print("Dictionary 4".center(50,"*"))
for key,val in d.items() :
    print(key)


d2 = [
    {"name":"samsung s6", "price":3000},
    {"name":"samsung s7", "price":4000},
    {"name":"samsung s8", "price":5000},
    {"name":"samsung s9", "price":6000},
    {"name":"samsung s10", "price":7000},
]
print("liste 2".center(50,"*"))
for key in d2 :
    print(key)
    
print("liste 3".center(50,"*"))
for key in d2 :
    print(key["name"])


    