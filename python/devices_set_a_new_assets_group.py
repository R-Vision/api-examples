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

# id можно перечислять через запятую для обновления нескольких устройств
# для получения id устройств, смотри devices_get_all.py
deviceData = {
    'id': [3853],
    'values': {
        # Идентификаторы групп ИТ-активов, перечень всех ИТ-групп можно узна,
        # выполнив GET запрос api/v1/am/assets
        'assets_id': [1958, 3617, 5081]
    }
}

device = s.put(
    PROTOCOL + '://' + RVISION + '/api/v1/am/devices',
    data=json.dumps(deviceData),
    verify=False
)

deviceResult = device.json()

print json.dumps(deviceResult, indent=2, sort_keys=True, ensure_ascii=False)
