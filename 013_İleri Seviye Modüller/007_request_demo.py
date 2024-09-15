import json
import requests
import json

api_key = "922e46af4b1e6095bbd57af9"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
kur = "USD"
response = requests.get(api_url+kur)

print(type(response))
to_json = json.loads(response.text)

for key, value in to_json["conversion_rates"].items() :
    print(f"{key} : {value} ")



