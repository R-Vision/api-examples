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

statuses = s.get(
    PROTOCOL + '://' + RVISION + '/api/v1/im/directories/status/17',
    params={
        'withoutHidden': False  # Включаем скрытые статусы
    },
    verify=False
)

statusesResult = statuses.json()

print json.dumps(statusesResult, indent=2, sort_keys=True, ensure_ascii=False)
