import sys
import os
import site


def is_in_venv() -> bool:
    """
    Check if the script is running inside a virtual environment.
    Returns:
        bool: True if in venv, False otherwise.
    """
    # Check if sys.prefix is different from sys.base_prefix
    return (
        hasattr(sys, 'real_prefix') or
        (sys.base_prefix != sys.prefix)
    )


def main() -> None:
    """
    Detect and display the current Matrix (environment) status.
    """
    try:
        in_venv: bool = is_in_venv()
        #It shows the executable python path
        python_executable: str = sys.executable
        # Get package installation path
        package_path: list[str] = site.getsitepackages()

        if not in_venv:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {python_executable}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate  # On Unix")
            print("matrix_env\\Scripts\\activate      # On Windows")
        else:
            venv_path: str = sys.prefix
            venv_name: str = os.path.basename(venv_path)
            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {python_executable}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {venv_path}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print(f"\nPackage installation path:\n{package_path[0]}")

    except Exception as e:
        print(f"An error occurred while detecting the environment: {e}")


if __name__ == "__main__":
    main()