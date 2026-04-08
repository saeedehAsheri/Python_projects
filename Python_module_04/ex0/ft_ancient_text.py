"""
Docstring for ex0.ft_ancient_text.
"""


def main():
    """
    Recover data from the ancient fragment file.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")

        content = file.read()

        print("RECOVERED DATA:")
        print(content)

        file.close()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
