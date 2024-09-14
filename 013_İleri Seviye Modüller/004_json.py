import json

# result = dir(json)

person = {
    "name":"Sinan",
    "diller":["C","C++","PHP"]
}

person_string = '{"name":"Sinan", "diller":["C","C++","PHP"]}'

# result = person["name"]
# result = person["diller"]
# result = person["diller"][0]


# json to dict
# result = json.loads(person_string)
# print(type(result))

# result = person["name"]
# result = person["diller"][0]

# with open("person.json") as f :
#     data = json.load(f)
#     print(data)
#     print(data["name"])


# dict to json
result = json.dumps(person, indent=4, sort_keys=True)
result = json.dumps(person)

print(result) 
print(type(result)) # str


with open("person_2.json" ,"w") as f :
    json.dump(person, f)


# print(result)