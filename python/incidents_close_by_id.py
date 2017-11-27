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

# id инцидентов можно перечислять через запятую для закрытия нескольких инцидентов
# нужно обязательно указать дату в формате (YYYY-MM-DD) и время закрытия, а также причину
incidentData = {
    'ids': [440],
    'completion': '2017-04-16',
    'tcompletion': '23:26:00',
    'message': 'Причина закрытия'
}

# POST запрос на закрытие инцидента
incident = s.post(
    PROTOCOL + '://' + RVISION + '/api/v1/im/incidents/close_incidents',
    data=json.dumps(incidentData),
    verify=False
)

incidentResult = incident.json()

incident = s.post(
    PROTOCOL + '://' + RVISION + '/api/v1/im/incidents/close_incidents',
    data=json.dumps(incidentData),
    verify=False
)

incidentResult = incident.json()

print json.dumps(incidentResult, indent=2, sort_keys=True, ensure_ascii=False)
