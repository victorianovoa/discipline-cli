import json
from pathlib import Path

FILE_PATH = Path("data/data.json")

def load_data():
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    FILE_PATH.parent.mkdir(exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)