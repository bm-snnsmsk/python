import requests


# themoviedb.org
# bm-snnsmsk
# best.221727
# eemsinan.73@gmail.com

# pip install tmdb3

# https://developer.themoviedb.org/docs/getting-started

my_api_key = "0cd3b625da34a8cedab76dcee994505d"
api_url = f"https://api.themoviedb.org/3/movie/157336?api_key={my_api_key}"

response = requests.get(api_url)

# print(type(response))
# print(response)
print(response.text)
