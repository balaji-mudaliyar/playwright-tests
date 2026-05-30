import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / 'reports'
SCREENSHOT_DIR = REPORT_DIR / 'screenshots'
ENV_FILE = BASE_DIR / 'config' / 'env.json'


def get_config() -> dict:
    with ENV_FILE.open() as f:
        return json.load(f)
