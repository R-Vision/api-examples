#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

PROTOCOL = 'http'  # or https
RVISION = '127.0.0.1'  # ip or hostname
USERNAME = 'admin'  # any user login
PASSWORD = 'admin'

requests.packages.urllib3.disable_warnings()

s = requests.Session()

# Авторизируемся
login = s.post(
    PROTOCOL + '://' + RVISION + '/login',
    data={
        'username': USERNAME,
        'password': PASSWORD
    },
    verify=False
)

loginResult = login.json()

# Применяем пагинацию и лимит
orgParams = {
    'page': 1,  # Пагинация, номер страницы
    'start': 0,  # Пагинация, позиция элемента с которого начать поиск
    'limit': 50  # Сколько всего выводить
}

# Следующая страница
# orgParams = {
#    'page': 2,
#    'start': 10,
#    'limit': 10
# }

# Вывести все (может быть очень долго)
# orgParams = {
#    'page': 1,
#    'start': 0,
#    'limit': 999999  # Итоговое количество может быть ограничено лицензией
# }

org = s.get(
    PROTOCOL + '://' + RVISION + '/api/v1/am/organization',
    params=orgParams,
    verify=False
)

orgResult = org.json()

print json.dumps(orgResult, indent=2, sort_keys=True, ensure_ascii=False)
