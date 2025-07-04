import requests

# pip install requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)
# <Response [200]>
# 2xx ok
# 3xx warningi
# 4xx - 404 - brak strony, 400 Bad Request - bład w parametrach, 401 - bład autoryzacji
# 5xx - błedy po stronie serwera, 500 Internal Server Error
# print(response.headers) # nagłówek

print(response.text)
# {"categories":[],"created_at":"2020-01-05 13:42:26.447675",
# "icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png",
# "id":"5WodmFzySCKkWxuy1YqYJQ","updated_at":"2020-01-05 13:42:26.447675",
# "url":"https://api.chucknorris.io/jokes/5WodmFzySCKkWxuy1YqYJQ",
# "value":"Chuck Norris once rocked so hard in an AC/DC concert that it was felt even in 1906. They called it the great San Francisco earthquake."}

data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'categories': [], 'created_at': '2020-01-05 13:42:24.696555',
#  'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png', 'id': 'nVeolCAvQ0qH7E4eSrigoA',
#  'updated_at': '2020-01-05 13:42:24.696555', 'url': 'https://api.chucknorris.io/jokes/nVeolCAvQ0qH7E4eSrigoA',
#  'value': 'Chuck Norris was recently asked what he thought of Nancy Pelosi? Chuck said he thinks Nancy Pelosi is uglier than a bucket of buttholes. There were no further questions.'}

# wypisac klucze ze słownika
print(data.keys())
# dict_keys(['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])
for k in data:  # wypisuje klucze
    print(k)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value
print(data['value'])
print(data.get('value'))
# Aliens have been abducted by Chuck Norris.
# Aliens have been abducted by Chuck Norris.

response_img = requests.get(data['icon_url'])
with open('icona.jpg', 'wb') as f:
    f.write(response_img.content)
print("Zdjęcie zostało zapisane")
