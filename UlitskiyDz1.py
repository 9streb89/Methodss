"""1.Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для
конкретного пользователя, сохранить JSON-вывод в файле *.json"""

# https://api.github.com/users/USERNAME/repos
# #нахожу список репозиториев своего аккаунта в Гитхабе.

import requests
import json
from pprint import pprint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
url = 'https://api.github.com/users/9streb89/repos'


response = requests.get(url, headers=headers)
j_data = response.json()

pprint(f"У пользователя {j_data[0].get('owner').get('login')} есть репозитории: {j_data[0].get('name')} \
, {j_data[1].get('name')} и {j_data[2].get('name')}")

# with open('repo.json', 'w') as f:
#     json.dump(j_data, f)
