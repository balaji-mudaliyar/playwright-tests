# Playwright Tests

A Playwright Python test repository scaffold with a POM-friendly layout.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m playwright install
```

## Run tests

```bash
pytest
```

## Structure

```text
playwright-tests/
│
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_checkout.py
│   │
│   ├── api/
│   │   ├── test_users_api.py
│   │
│   └── test_smoke.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
   ├── home_page.py
│   └── checkout_page.py
│
├── fixtures/
│   ├── browser_fixture.py
│   ├── auth_fixture.py
│
├── utils/
│   ├── config.py
│   ├── helpers.py
│   ├── test_data.py
│
├── config/
│   ├── env.json
│   ├── settings.py
│
├── reports/
│   ├── html/
│   ├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## Notes

- `tests/ui/` contains UI Playwright tests
- `tests/api/` contains API-level tests
- `pages/` contains page objects
- `fixtures/` contains pytest fixtures
- `utils/` contains helper modules and test data
- `config/` contains environment and settings files
- `reports/` is a placeholder for HTML reports and screenshots
