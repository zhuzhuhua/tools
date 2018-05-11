# -*- coding: UTF-8 -*-
import requests
url = ""
headers = {
    'Authorization': 'token',
    'Content-Type': 'application/json',
}

response = requests.get(url=url, headers=headers)
