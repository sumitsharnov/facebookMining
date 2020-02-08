import requests

studentdetails = requests.get("https://dhcr.clarin-dariah.eu/api/v1/institutions/index?sort_count").json()
print(studentdetails)
for s in studentdetails:
    print(s['city']['id'])