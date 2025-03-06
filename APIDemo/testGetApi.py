import requests
import json
import pytest

endpoint = "https://reqres.in/api/users/2";

# test word should be present in method name to execute by pytest
def test_get_API_endpoint():
    response = requests.get(endpoint)
    print(response.text)
    assert response.status_code == 200

