from typing import Any
import json
from pathlib import Path
from pydantic import ValidationError
from src.errors import InputFileError
from src.models import FunctionCall, FunctionCallResult, FunctionDefinition

def load_json_file(path: Path)-> Any:
    """
    reading the JSON file
    """
    try:
        with open(path, "r") as file:
            data = json.load(file)
            #print("data: ", data)
            return data
    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")

def write_json_file(path: Path, results: list[FunctionCallResult])-> None:
    """Write valid results into a JSON file."""

    path.parent.mkdir(parents= True, exist_ok= True)

    data = [res.model_dump() for res in results]
    try:
        with open(Path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent= 2, ensure_ascii= False)
    except OSError:
        print(f"Couldn't write output file to '{path}'")

def load_func_def(path: Path)-> list[FunctionDefinition]:
    """Load and validate function definition from JSON"""
    file = load_json_file(path)
    if not isinstance(file, list):
        raise InputFileError("Function definitions file must contain a JSON array.")
    try:
        return [FunctionDefinition.model_validate(item) for item in file]
    except ValidationError as exc:
        raise InputFileError(f"Invalid function definitions schema: {exc}") from exc

def load_func_call(path: Path)-> list[FunctionCall]:
    "Load and validate function calls (prompts) from Json"
    file = load_json_file(path)
    
    if not isinstance(file, list):
        raise InputFileError("Prompt input file must contain a JSON array.")
    
    try:
        return [FunctionCall.model_validate(item) for item in file]
    except ValidationError as exc:
        raise InputFileError(f"Invalid prompt input schema: {exc}") from exc
