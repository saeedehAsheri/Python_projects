from typing import Any
import json
from pathlib import Path
from pydantic import ValidationError
from models import FunctionCall, FunctionCallResult, FunctionDefinition

def load_json_file(path: Path)-> Any:
    """
    reading the JSON file
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

def write_json_file(path: Path, results: list[FunctionCallResult])-> None:
    """Write valid results in a JSON file."""

    path.parent.mkdir(parents= True, exist_ok= True)

    data = [res.model_dump() for res in results]
    try:
        with open(Path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent= 2, ensure_ascii= False)
    except OSError:
        print(f"Couldn't write output file to '{path}'")


