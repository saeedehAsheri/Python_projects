import re
import itertools
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


def score_func_name(
        llm: LLMInterface,
        prompt: str,
        function_definition: FunctionDefinition,
        )-> float:
    """Use the LLM to score how well a function name matches the prompt."""
    ranking_prompt = (
        "You are a function-calling classifier.\n"
        "Given the user request and the function description, decide whether this "
        "function is the best match.\n\n"
        f"User request: {prompt}\n"
        f"Function name: {function_definition.name}\n"
        f"Function description: {function_definition.description}\n"
        "Answer:"  
    )
    return llm.compute_log_prob(ranking_prompt, "yes")


def choose_best_function(
        llm: LLMInterface,
        prompt: str,
        function_definitions: list[FunctionDefinition],
)-> FunctionDefinition:
    """to choose the best function using the llm"""
    if not function_definitions:
        raise DecodingError("No function definitions available")
    
    best_function = function_definitions[0]
    best_score = float("-inf")

    for func_def in function_definitions:
        score = score_func_name(llm, prompt, func_def)
        if score > best_score:
            best_score = score
            best_function = func_def
    
    return best_function

def generate_param_candidate_dicts(
        prompt: str,
        func_def : FunctionDefinition,
        max_cand_per_paramete: int = 5
)-> list[dict[str, Any]]:
    """Generate schema-shaped candidate parameter dictionaries."""
    param_names = list(func_def.parameters.keys())
    per_param_candidates: list[list[Any]] = []

    for param_name in param_names:
        expected_type = func_def.parameters[
            param_name
        ].type
        values = build_candidate_types(prompt, expected_type)
        per_param_candidates.append(
            values[:max_cand_per_paramete]
        )
    
    combinations = itertools.product(*per_param_candidates)
    candidate_dicts: list[dict[str, Any]] = []

    for combo in combinations:
        item = dict(zip(param_names, combo, strict=True))
        candidate_dicts.append(item)
    
    return candidate_dicts


def score_param_candidate(
        llm: LLMInterface,
        prompt: str,
        func_def: FunctionDefinition,
        parameters: dict[str, Any]
)-> float:
    """Score a candidate parameter assignment with the LLM."""
    candidate_prompt = (
    "You are evaluating a structured function call.\n"
    "Decide if the proposed function call correctly matches the user request.\n\n"
    f"User request: {prompt}\n"
    f"Function name: {function_definition.name}\n"
    f"Function description: {function_definition.description}\n"
    f"Candidate parameters: {parameters}\n"
    "Answer:"
    )
    return llm.compute_log_prob(candidate_prompt, " yes")


def choose_best_params(
        llm: LLMInterface,
        prompt: str,
        func_def: FunctionDefinition
)-> dict[str, Any]:
    """Choose the best parameter dictionary for a selected function."""
    candidates = generate_param_candidate_dicts(
        prompt,
        func_def
    )
    if not candidates:
        raise DecodingError(
            f"No parameter candidates generated for function '{func_def.name}'."
        )
    best_candidate = candidates[0]
    best_score = float("-inf")

    for candidate in candidates:
        try:
            validated = validate_params_against_schema(
                func_def, candidate
            )
        except ValueError:
            continue

        score = score_param_candidate(
            llm = llm,
            prompt= prompt,
            func_def= func_def,
            parameters= validated
        )
        if score > best_score:
            best_score = score
            best_candidate = validated

    try:
        return validate_params_against_schema(
            func_def, best_candidate
        )
    except ValueError as exc:
        raise DecodingError(
            f"Could not validate parameters for function '{func_def.name}'."
        ) from exc
