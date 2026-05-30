import requests


def test_get_users_api() -> None:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
