from src.decoder import choose_best_function, choose_best_params
from src.llm_interface import LLMInterface
from src.models import FunctionCallResult, FunctionDefinition, FunctionCall


def process_single_prompt(
        llm: LLMInterface,
        prompt_item: FunctionCall,
        func_def: list[FunctionDefinition]
)-> FunctionCallResult:
    """Process one prompt into a structured function call result."""
    func_definition = choose_best_function(
        llm= llm,
        prompt= prompt_item.prompt,
        function_definitions= func_def
    )

    parameters = choose_best_params(
        llm= llm,
        prompt= prompt_item.prompt,
        func_def= func_def
    )

    return FunctionCallResult(
        prompt= prompt_item.prompt,
        name= func_definition.name,
        parameters= parameters
    )

def process_all_prompts(
        llm: LLMInterface,
        prompt_items: list[FunctionCall],
        func_defs: list[FunctionDefinition]
)-> list[FunctionCallResult]:
    """Process all prompts into structured results."""

    results: list[FunctionCallResult] = []

    for prompt_item in prompt_items:
        result = process_single_prompt(
            llm= llm,
            prompt_item= prompt_item,
            func_def= func_defs
        )
        results.append(result)

    return results