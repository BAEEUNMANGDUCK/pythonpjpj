import requests
import datetime as dt


USERNAME = "blahblah"
TOKEN = "blah"
GRAPH_ID = "blah"

PIXELA_ENDPOINT = "https://pixe.la/v1/users" 
GRAPH_ENDPOINT = "https://pixe.la/v1/users/" + USERNAME + "/graphs"


today = dt.datetime.now().strftime("%Y%m%d")


create_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


# TODO  유저 생성

# create_user_response = requests.post(url="https://pixe.la/v1/users", json=create_params)
# print(create_user_response.text)


# TODO 그래프 생성 (Request Header 필요, 스니핑을 피하기 위해)

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_config = {
    "id":GRAPH_ID,
    "name":"Exercising graph",
    "unit":"calory",
    "type":"int",
    "color":"momiji"
}

# create_graph_response = requests.post(url=GRAPH_ENDPOINT,json=graph_config, headers=headers)
# print(create_graph_response.text)

# TODO 그래프에 픽셀에 값 전달 
value_config = {
    "date":str(today),
    "quantity": input("How many calories did you burned?"),
}
# graph_value_response = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=value_config, headers=headers)

# print(graph_value_response.text)


# TODO 그래프 픽셀 값 수정 

update_config = {
    "quantity":"1000"
}

# pixel_update_response = requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{today}", json=update_config, headers=headers)

# print(pixel_update_response.text)

# TODO 그래프 픽셀 값 삭제 

pixel_delete_response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/20230802", headers=headers)
print(pixel_delete_response.text)