import re
from typing import Any
from src.errors import DecodingError
from src.llm_interface import LLMInterface
from src.models import FunctionDefinition
from src.schema_utils import validate_params_against_schema

_NUM_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")
_SINGLE_QUOTED_PATTERN = re.compile(r"'([^']*)'")
_DOUBLE_QUOTED_PATTERN = re.compile(r'"([^"]*)"')
_WORD_PATTERN = re.compile("\b[A-Za-z_][A-Za-z0-9_-]*\b")

def extract_numbers(prompt: str)-> list[float]:
    """Extract numbet candidates from prompt"""
    numbers: list[float] = []
    for num in _NUM_PATTERN.findall(prompt):
        try:
            numbers.append(float(num))
        except ValueError:
            continue
    return numbers

def extract_strings(prompt: str)-> list[str]:
    """Extract strings from the given prompts"""
    strings: list[str] = []

    for singleq_w in _SINGLE_QUOTED_PATTERN.findall(prompt):
        try:
            strings.append(singleq_w)
        except ValueError:
            continue

    for doubleq_w in _DOUBLE_QUOTED_PATTERN.findall(prompt):
        try:
            strings.append(doubleq_w)
        except ValueError:
            continue
    
    words = _WORD_PATTERN.findall(prompt)

    for word in words:
        lowered = word.lower()
        if lowered in {
            "what",
            "is",
            "the",
            "sum",
            "of",
            "and",
            "greet",
            "reverse",
            "string",
            "calculate",
            "square",
            "root",
            "replace",
            "all",
            "numbers",
            "with",
            "vowels",
            "substitute",
            "word",
            "in",
        }:
            continue
        strings.append(word)
    
    avoid_dup: list[str] = []
    for s in strings:
        if s not in avoid_dup:
            avoid_dup.append(s)
    
    return avoid_dup

def extract_booleans(prompt: str)-> list[bool]:
    """Extract boolean candidates from the prompt"""
    lowered: str = prompt.lower()
    booleans: list[bool] = []

    if "true" in lowered or "yes" in lowered:
        booleans.append(True)
    if "false" in lowered or "no" in lowered:
        booleans.append(False)

    return booleans

def build_candidate_types(prompt: str, expected_type: str)-> list[Any]:
    """Build candidate values for prameter type from a prompt"""
    if expected_type == "number":
        values = extract_numbers(prompt)
        return values if values else [0.0]
    
    if expected_type == "string":
        values = extract_strings(prompt)
        if not values:
            stripped = prompt.strip()
            return [stripped]
        return values
    
    if expected_type == "boolean":
        values = extract_booleans(prompt)
        return values if values else [False, True]
    
    raise DecodingError(f"Unsupported parameter type: {expected_type}")





