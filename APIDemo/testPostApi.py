import requests
import json
import pytest

endpoint = "https://reqres.in/api/users"

payload = {
    "name": "morpheus",
    "job": "leader"
}
def test_post_API_endpoint():
    response = requests.post(endpoint, payload)
    # json_response = json.loads(response.text)
    json_response = response.json()
    print("Response")
    for key, value in json_response.items():
        print(f"Key: {key}, Value: {value}")
    assert response.status_code == 201

    id = json_response["id"]
    if id is not None:
        print(id)
        assert json_response["name"] == "morpheus"
        assert json_response.get("job") == "leader"

    else:
        print("id not found")
