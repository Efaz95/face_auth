import requests
import json

headers = {
	'Content-Type': 'application/json',
    "app_id": "a7a35024",
    "app_key": "9a5b0048d2643e34d31b855d8fedf8e2"
}

values1 ="""{
    "image": "https://icc-corp-2013-live.s3.amazonaws.com/players/284/201.png",
    "subject_id": "Sakib",
    "gallery_name": "gallery1"
  }"""


values2 ="""{
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSRQO8xC2iCHJ5qpsGGoZOgwjTwmS1roJr3cOsVYnWNP3zCQR82w",
    "subject_id": "Sakib",
    "gallery_name": "gallery1"
  }"""

values3 = """
  {
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5yo6WP7CXtr_iMzrpChC70Pz9w4QAPrQygV-Kt7V_pTw1j9IIdA",
    "gallery_name": "gallery1"
  }
"""

values3 = """
  {
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5yo6WP7CXtr_iMzrpChC70Pz9w4QAPrQygV-Kt7V_pTw1j9IIdA",
    "gallery_name": "gallery1"
  }"""

# response1 = requests.post('https://api.kairos.com/enroll', data=values1, headers=headers)
# print(response1.json())

# response2 = requests.post('https://api.kairos.com/verify', data=values2, headers=headers)
# confidence = response2.json()['images'][0]['transaction']['confidence']
# print(confidence)
response3 = requests.post('https://api.kairos.com/recognize', data=values3, headers=headers)
# print(response3.json())


response4 = requests.post('https://api.kairos.com/detect', data=values3, headers=headers)
print(response4.json())

