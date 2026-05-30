from playwright.sync_api import Playwright, APIRequestContext
import pytest


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    headers={"Content-Type" : "application/json"}
    request_context=  playwright.request.new_context(base_url="http://localhost:8080", extra_http_headers=headers)
    yield request_context
    request_context.dispose()