from playwright.sync_api import Playwright, APIRequestContext
import pytest
import os


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    headers = {"Content-Type": "application/json"}
    base_url = os.getenv("TEST_SERVICE_BASE_URL", "http://localhost:8080")
    request_context = playwright.request.new_context(
        base_url=base_url,
        extra_http_headers=headers,
    )
    yield request_context
    request_context.dispose()