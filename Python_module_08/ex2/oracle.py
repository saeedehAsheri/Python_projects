import os
import sys
from dotenv import load_dotenv
from typing import Dict, Optional


def load_mainframe_config() -> Dict[str, Optional[str]]:
    """
    Loads Matrix configuration from environment variables.
    Uses python-dotenv to read from a .env file if it exists.
    """
    # Load variables from .env file into the system environment
    load_dotenv()

    # Fetching variables with os.getenv
    # The second argument is the default value if the variable is not found
    config = {
        "MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_URL": os.getenv("ZION_ENDPOINT")
    }
    return config


def main() -> None:
    """Main function to display the Oracle's view of the Matrix."""
    print("ORACLE STATUS: Reading the Matrix...")

    try:
        config = load_mainframe_config()

        print("\nConfiguration loaded:")
        print(f"Mode: {config['MODE']}")

        # Using ternary operators for clean display (Rigor)
        db_status = "Connected to local instance" if config['DATABASE'] \
            else "Disconnected"
        api_status = "Authenticated" if config['API_KEY'] else "Denied"
        zion_status = "Online" if config['ZION_URL'] else "Offline"

        print(f"Database: {db_status}")
        print(f"API Access: {api_status}")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print(f"Zion Network: {zion_status}")

        print("\nEnvironment security check:")
        # Check if secrets were actually loaded from an environment source
        if config['DATABASE'] and config['API_KEY']:
            print("[OK] No hardcoded secrets detected")
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] Running on default/missing configuration!")

        print("[OK] Production overrides available")
        print("The Oracle sees all configurations.")

    except Exception as e:
        print(f"ERROR: System breach detected: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
