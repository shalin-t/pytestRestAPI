import requests
import json
import pytest

endpoint = "https://reqres.in/api"

payload = {
    "name": "morpheus",
    "job": "assistant"
}

def test_put_request():
    response = requests.put(endpoint + "/users/2", payload)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)
    assert json_response["job"] == "assistant"
