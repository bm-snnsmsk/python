import json
import requests
import json

# print(json.__file__)

response = requests.get("https://jsonplaceholder.typicode.com/todos")

# print(response) # <Response [200]>
# print(response.text)
# print(type(response.text))  # <class 'str'>
# print(type(response.text[0]["title"]))  # json verilerine dict gibi erişilemez hata verir
# o yüzden convert etmek lazım

to_json = json.loads(response.text)
# print(to_json)
# print(to_json[0]["title"])

for i in to_json :
    # print(i)
    print(i["title"])



