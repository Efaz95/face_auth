import os
import requests
import json

APP_KEY = os.environ.get('KAIROS_API')

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

response1 = requests.post('https://api.kairos.com/enroll', data=values1, headers=headers)
print(response1.json())

