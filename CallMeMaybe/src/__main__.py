from pathlib import Path
from cli import pars_args
from io_utils import load_json_file

def main():
    """
    parser = argparse.ArgumentParser(
        description= "The program for using llm",
        usage= "uv run python -m src [--functions_definition <function_definition_file>]"
        " [--input <input_file>] [--output <output_file>]")
    parser.add_argument(action= "-o")
    parser.parse_args()
    """
    parser = pars_args()
    func_def = load_json_file(parser.functions_definition)
    #print(func_def)


if __name__ == "__main__":
    main()