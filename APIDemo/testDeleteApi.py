import requests
import json
import pytest

endpoint = "https://reqres.in/api/users/2"

def test_delete_request():
    response = requests.delete(endpoint)
    print(f"response: {response.text}")
    print("------")
    try:
        json_response = response.json()
        print(json_response)
    except:
        print("no response")

    assert response.status_code == 204