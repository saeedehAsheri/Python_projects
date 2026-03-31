from typing import Any
import json
from pathlib import Path

def load_json_file(path: Path)-> Any:
    """
    """
    try:
        with open(path, "r") as file:
            data = json.load(file)
            print("data: ", data)
            return data
    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
