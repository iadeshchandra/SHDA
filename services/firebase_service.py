import requests

BASE_URL = "https://shda-6245c-default-rtdb.asia-southeast1.firebasedatabase.app/"

def push(path, data):
    requests.post(BASE_URL + path + ".json", json=data)