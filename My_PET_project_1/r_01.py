import requests
url = 'https://ya.ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)