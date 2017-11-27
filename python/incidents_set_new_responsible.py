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

# id можно перечислять через запятую для обновления нескольких инцидентов
# для получения id пользователей, запусти скрипт users_get_all.py
incidentData = {
    'id': [451],
    'values': {
        'responsible_id': 1  # Идентификатор пользователя
    }
}

incident = s.put(
    PROTOCOL + '://' + RVISION + '/api/v1/im/incidents',
    data=json.dumps(incidentData),
    verify=False
)

incidentResult = incident.json()

print json.dumps(incidentResult, indent=2, sort_keys=True, ensure_ascii=False)
