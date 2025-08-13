import requests
import datetime

pixela_endpoint="https://pixe.la/v1/users"

USERNAME="manav1298567425"
TOKEN="brocklesnar1298pookie"
id="graph1"
name="Cycling Graph"

user_params={
    "token":USERNAME,
    "username":TOKEN,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=user_params)
#
# print(response)
# print(response.status_code)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":id,
    "name":name,
    "unit":"Km",
    "type":"float",
    "color":"momiji",
}

headers={
    "X-USER-TOKEN":TOKEN
}

# response_graph=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response_graph.text)

pixel_post_endpoint=f"{graph_endpoint}/{id}"

today=datetime.datetime(year=2025,month=8,day=12)

print(today)

quantity="15"

pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":quantity,
}

# response_pixel=requests.post(url=pixel_post_endpoint,json=pixel_config,headers=headers)
# print(response_pixel.text)

update_and_delete_endpoint=f"{pixel_post_endpoint}/{today.strftime("%Y%m%d")}"

update_config={
    "quantity":"6"
}

# response_update=requests.put(url=update_and_delete_endpoint,json=update_config,headers=headers)
# print(response_update.text)

response_delete=requests.delete(url=update_and_delete_endpoint,headers=headers)
print(response_delete.text)








