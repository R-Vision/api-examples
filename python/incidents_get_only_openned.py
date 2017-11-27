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

# 1 - Обработка
# 2 - Расследование
# 3 - Закрыт
# 4 - Зарегистрирован
# 5 - Назначен
# Чтобы получить список всех статусов, выполни скрипт get_all_statuses.py

incidentsFilter = [{
    'operator': 'in',
    'property': 'status_id',
    'value': [1, 2, 4, 5]
}]

# Применяем пагинацию, лимит и фильтры
incidentsParams = {
    'page': 1,
    'start': 0,
    'limit': 10,
    'filter': json.dumps(incidentsFilter)
}

# Вывести все инциденты (может быть очень долго)
# incidentsParams = {
#    'page': 1,
#    'start': 0,
#    'limit': 999999,
#    'filter': json.dumps(incidentsFilter)  # Итоговое количество может быть ограничено лицензией
# }

incidents = s.get(
    PROTOCOL + '://' + RVISION + '/api/v1/im/incidents',
    params=incidentsParams,
    verify=False
)

incidentsResult = incidents.json()

print json.dumps(incidentsResult, indent=2, sort_keys=True, ensure_ascii=False)
