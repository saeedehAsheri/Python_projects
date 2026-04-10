"""
Writing some function which are useful
to make the JSON output reliable according to the
project. These functions help us to avoid a wrong 
output.
"""

from typing import Any

from src.models import FunctionDefinition

def get_func_by_name(
        func_defs: list[FunctionDefinition],
        name: str
)-> FunctionDefinition | None:
    "Try to find function definition by name"

    for func_def in func_defs:
        if func_def.name == name:
            return func_def
    return None

def normalize_param_value(expected_type: str, value: Any)-> Any:
    """Convert the value to expected JSON schema type"""
    if expected_type == "string":
        return str(value)
    
    if expected_type == "number":
        if isinstance(value, bool):
            raise ValueError("Boolean can not converted to number here.")
        return float(value)
    
    if expected_type == "boolean":
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in {"yes", "true", "1"}:
                return True
            if lowered in {"no", "false", "0"}:
                return False
        raise ValueError(f"Can not convert the {value!r} to boolean")
    
    raise ValueError(f"Unsupported parameter type: {expected_type}")

def validate_params_against_schema(
        func_defs: FunctionDefinition,
        parameters: dict[str, Any]
)-> dict[str, Any]:
    """Validate and normalize parameters according to the function schema"""
    normalize: dict[str, Any]= {}

    for param_name, param_spec in func_defs.parameters.items():
        if param_name not in parameters:
            raise ValueError(
                f"Missing required parameter '{param_name}' for function"
                f"'{func_defs.name}'"
            )
        normalize[param_name] = normalize_param_value(
            param_spec.type,
            parameters[param_name],
        )
    if set(parameters.keys()) != set(func_defs.parameters.keys()):
        raise ValueError(
            f"Unexpected parameters for function '{func_defs.name}'"
        )
    return normalize
