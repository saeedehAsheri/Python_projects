import argparse
from pathlib import Path

def pars_args()-> argparse.Namespace:
    """
    A function for read and pars argument from the command line.
    """
    parser = argparse.ArgumentParser(
        description= "Translate natural language prompts into structured function calls."
        )
    parser.add_argument(
        "--functions_definition", 
        help="Path to the JSON file containing function definitions.", 
        type= Path,
        default="data/input/functions_definition.json",
        )
    parser.add_argument(
        "--input",       
        help="Path to the JSON file containing input prompts.", 
        type= Path,
        default="data/input/function_calling_tests.json",
        )
    parser.add_argument(
        "--output",
        help="Path to the JSON output file.",
        type= Path,
        default="data/output/function_calling_results.json",
        )
    args = parser.parse_args()

    return args