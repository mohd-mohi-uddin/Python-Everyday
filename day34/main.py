import requests
from datetime import datetime

USERNAME = "asim09"
TOKEN = "fjdnjvnfnjnfjvdnjncn"
GRAPHID = "graph1"

user_endpoint= "https://pixe.la/v1/users"

user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= user_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "workout graph",
    "unit": "hours",
    "type": "float",
    "color": "ichou"
}

header= {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(response.text)

pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime(year= 2026,month= 7, day= 28)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers= header)
# print(response.text)

update_pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPHID}/20260729"

update_pixel_config = {
    "quantity": "12"
}

update_color = {
    "color": "momiji"
}

response = requests.put(url= pixel_endpoint, json=update_color, headers= header)
print(response.text)

