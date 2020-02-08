import json

import requests

data = requests.get("https://dhcr.clarin-dariah.eu/api/v1/countries/index").json()
#names = [student['name'] for student in data['name']]
for studentdetail in data:
    print(studentdetail['id'])
    print(studentdetail['name'])



