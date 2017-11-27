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

# Перечень всех дополнительных полей сервер возвращает в ответе
deviceData = {
    'name': 'Наименование узла',
    'nodes_id': 1,  # Тип узла "Нераспознанный узел". Другие типы можно узнать, сделав GET запрос к api/v1/am/nodes
    'device_ips': [{
        'ip': '192.168.0.1'  # в этот объект можно добавить поля mac и mask
    }],
}

device = s.post(
    PROTOCOL + '://' + RVISION + '/api/v1/am/devices',
    data=json.dumps(deviceData),
    verify=False
)

deviceResult = device.json()

print json.dumps(deviceResult, indent=2, sort_keys=True, ensure_ascii=False)
