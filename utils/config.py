import json
from pathlib import Path


def load_env() -> dict:
    path = Path(__file__).parent.parent / 'config' / 'env.json'
    return json.loads(path.read_text())
