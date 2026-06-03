import pytest
from playwright.sync_api import Playwright, APIRequestContext
import requests
import uuid

def test_get_users_api(api_request_context: APIRequestContext) -> None:
    users = api_request_context.get("/users/1")
    assert users.status == 200
    expected_json = {"id": 1, "name": "John Doe", "email": "john@test.com"}
    assert users.json() == expected_json


def test_create_user_api(api_request_context:APIRequestContext) -> None:
    unique_email = f"alice+{uuid.uuid4().hex[:8]}@test.com"
    payload = {"name": "Alice", "email": unique_email}
    response = api_request_context.post(
        '/create-user',
        data=payload
    )
    assert response.status == 201
    assert response.json().get('name') == 'Alice'
    assert response.json().get('email') == unique_email
    assert 'id' in response.json()


def test_get_missing_user_api(api_request_context: APIRequestContext) -> None:
    response= api_request_context.get('/users/999')
    assert response.status == 404


def test_get_all_users_api(api_request_context:APIRequestContext) -> None:
    response = api_request_context.get('/users')
    assert response.status == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) >= 0