from pathlib import Path
from src.cli import parse_args
from src.io_utils import (
    load_json_file,
    write_json_file,
    load_func_call
)
from src.llm_interface import LLMInterface
from src.pipeline import process_all_prompts
from src.errors import ProjectError
import sys

def main():
    """
    Run the application
    """
    args = parse_args()

    try:
        func_defs = load_json_file(args.functions_definition)
        prompt_items = load_func_call(args.input)

        llm = LLMInterface()
        
        results = process_all_prompts(
            llm= llm,
            prompt_items= prompt_items,
            func_defs= func_defs
        )

        write_json_file(args.output, results)
        print(f"Successfully wrote {len(results)} results to: {args.output}")
    except ProjectError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Unexpected error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()