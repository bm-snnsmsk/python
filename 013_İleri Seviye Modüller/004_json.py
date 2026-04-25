import json

# result = dir(json)

person = {
    "name":"Sinan",
    "diller":["C","C++","PHP"]
}

person_dictionary = {"name":"Sinan", "diller":["C","C++","PHP"]}
person_json_string = '{"name":"Sinan", "diller":["C","C++","PHP"]}'

# result = person["name"]
# result = person["diller"]
# result = person["diller"][0]


# json stringi to dict
# result = json.loads(person_json_string)
# print(type(result))  ## json stringi artık dictionary

# result = person["name"]
# result = person["diller"][0]


# person.json >>> {"name":"Sinan", "diller":["C","C++","PHP"]}
# with open("person.json") as f :
#     data = json.load(f)
#     print(data)
#     print(data["name"])

########################################################################
person_dict = {
    "name":"Sinan",
    "diller":["C","C++","PHP"]
}
# dict to json
result = json.dumps(person_dict, indent=4, sort_keys=True)  ## konsolda okunurluğu düzgün olsun diye eklenen parametreler
result = json.dumps(person_dict)   ### dictionaty artık string olduğu için person_dict["name"]  hat verecektir artık

print(result) 
print(type(result)) # str


with open("person.json" ,"w") as f :
    json.dump(person_dict, f)


# print(result)
