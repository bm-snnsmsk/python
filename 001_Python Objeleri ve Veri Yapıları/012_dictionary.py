# key - value

# liste = []
# dictionary = {}
# tuple = ()

dict = {
    "kocaeli" : 41,
    "istanbul" : 34,
    "izmir" : 35,
    "şırnak" : 73,
    "mardin" : 47,
}

dict["siirt"] = 56
dict["kocaeli"] = "new value" 

print(dict["kocaeli"])



## dictionary içinde dictionary, dictionary içinde list

users = {
    'sinan' :{"roles":["admin,user"],'age':39,"email":"snnsmsk@gmail.com","address":"mardin"} ,
    'baran' :{"roles":["user"],'age':3,"email":"brn@gmail.com","address":"mardin"} ,
    'emine' :{"roles":["user"],'age':28,"email":"emine@gmail.com","address":"mardin"} ,
    'tuba'  :{"roles":["user"],'age':7,"email":"tuba@gmail.com","address":"mardin"} ,
}
print(users.keys())

print(users["sinan"]["age"])
print(users["baran"]["age"])
print(users["emine"]["roles"])

users["nujin"] = {"roles":["user"],'age':12,"email":"nujin@gmail.com","address":"silopi"}

print(users.keys())
users.update({'kendal' :{"roles":["user"],'age':10,"email":"kendal@gmail.com","address":"silopi"}})
print(users.keys())
users.update({"mehmet":{}})
print(users.keys())

print(users["mehmet"])
print(users["mehmet"]["age"])


