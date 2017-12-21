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

# Идентификатор инцидента
incidentId = 1

organizationData = [{
    'id': 1,  # Идентификатор организации (organizations_get_all.py)
    'checked': True  # Привязать организацию к инциденту
}, {
    'id': 2,  # Идентификатор организации (organizations_get_all.py)
    'checked': False  # Удалить привязку к организации
}]

incidentData = {
    'ids': json.dumps(organizationData)
}

incident = s.put(
    PROTOCOL + '://' + RVISION + '/api/v1/im/incidents/' + str(incidentId) + '/organizations',
    data=json.dumps(incidentData),
    verify=False
)

# Способ №2 (deprecated)

# Идентификатор организации (смотри organizations_get_all.py)
# organizationId = 1

# Добавление организации
# incident = s.post(
#     PROTOCOL + '://' + RVISION + '/api/v1/im/incidents/' + str(incidentId) + '/organizations/' + str(organizationId),
#     verify=False
# )

# Удаление организации
# incident = s.delete(
#     PROTOCOL + '://' + RVISION + '/api/v1/im/incidents/' + str(incidentId) + '/organizations/' + str(organizationId),
#     verify=False
# )

incidentResult = incident.json()

print json.dumps(incidentResult, indent=2, sort_keys=True, ensure_ascii=False)
