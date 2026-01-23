"""
Docstring for ex4.ft_crisis_response
"""


def handle_crisis(filename):
    """
    Attempt to access a file and handle specific errors.
    """
    print(f"CRISIS ALERT: Attempting access to '{filename}'")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly: {e}")
        print("STATUS: Crisis handled, system stable")


def main():
    """
    Execute the crisis response tests.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    handle_crisis("lost_archive.txt")
    handle_crisis("classified_vault.txt")
    handle_crisis("./standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
