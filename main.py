import requests
import json
from datetime import datetime as dt

USERNAME = "wallaceam"
TOKEN = "GEA79fdkank23nk"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "GEA79fdkank23nk",
    "username": "wallaceam",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Job Search Activity",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": "20221020",
    "quantity": "4",
    "optionalData": json.dumps("Wrote cover letter & submitted application")
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

today = dt.today()
today_formatted = today.strftime("%Y%m%d")
# print(today_formatted)

date_to_update = 20221020

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

update_config = {
    "quantity": "4.5"
}

response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

