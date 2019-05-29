#   python -m pip install requests

import requests
import json

stranka = requests.get('https://github.com')

# ověření, že dotaz proběhl v pořádku
stranka.raise_for_status()

# vypsání obsahu
print(stranka.text)

#----------------------

with open('token.txt') as soubor:
    token = soubor.read().strip()  


headers = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()
print(stranka.text)

# Tím, že jsi Githubu dal/a svůj token (načtený ze souboru, 
# předaný přes slovník headers), poznal,
#  že jde dotaz od tebe a vrátil nějaké informace ve formátu JSON.

data = json.loads(stranka.text)

print(json.dumps(data, ensure_ascii=True, indent=2))

print(data['avatar_url'])