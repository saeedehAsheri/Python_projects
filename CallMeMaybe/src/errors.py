class ProjectError(Exception):
    "Base exception for the project errors"

class InputFileError(ProjectError):
    """Raised when an input file is missing or invalid."""

class OutputFileError(ProjectError):
    """Raised when the output file cannot be written."""

class ModelError(ProjectError):
    """Raised when the llm-sdk have problem"""

class DecodingError(ProjectError):
    """Raised when the valid structured output cann't be produced."""