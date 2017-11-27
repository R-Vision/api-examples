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
devicesParams = {
    'page': 1,  # Пагинация, номер страницы
    'start': 0,  # Пагинация, позиция элемента с которого начать поиск
    'limit': 10  # Сколько всего выводить
}

# Следующая страница
# devicesParams = {
#    'page': 2,
#    'start': 10,
#    'limit': 10
# }

# Вывести все (может быть очень долго)
# devicesParams = {
#    'page': 1,
#    'start': 0,
#    'limit': 999999  # Итоговое количество может быть ограничено лицензией
# }

devices = s.get(
    PROTOCOL + '://' + RVISION + '/api/v1/am/devices',
    params=devicesParams,
    verify=False
)

devicesResult = devices.json()

print json.dumps(devicesResult, indent=2, sort_keys=True, ensure_ascii=False)
