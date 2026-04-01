from pydantic import BaseModel, ConfigDict, field_validator
from typing import Any, Literal

JsonScalarType = Literal["string", "number", "boolean"]

class Params(BaseModel):
    """Description of the function parameters"""
    model_config = ConfigDict()
    type: JsonScalarType

class ReturnsJson(BaseModel):
    """
    Description of the function returns
    """
    model_config = ConfigDict()
    type: JsonScalarType

class FunctionDefinition(BaseModel):
    """Function Definition loaded from JSON file"""
    model_config = ConfigDict()
    name: str
    description: str
    parameters: dict[str, Params]
    returns: Returns_json
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str)-> str:
        """Check if the value of the function name is not empty."""
        if not value.strip():
            raise ValueError("Function name can't be empty.")
        return value
    
    @field_validator("parameters")
    @classmethod
    def validate_parameters(cls, value: dict[str, Params])-> dict[str, Params]:
        """Checking the parameter map"""
        if not value.strip():
            raise ValueError("Function name can't be empty.")
        return value

class FunctionCall(BaseModel):
    """Function call prompts loaded from JSON file"""
    model_config = ConfigDict()
    prompt: str

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value: str)-> str:
        """To check prompt is not empty"""
        if not value.strip():
            raise ValueError("Prompt can't be empty.")
        return value

class FunctionCallResult(BaseModel):
    """Structured output for the result"""
    model_config = ConfigDict()
    prompt: str
    name: str
    parameters: dict[str, Any]
