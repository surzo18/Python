import requests

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.put('https://api.github.com/user/starred/pyvec/naucse.python.cz', headers=headers)
stranka.raise_for_status()