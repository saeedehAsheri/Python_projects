"""
Docstring for ex3.ft_vault_security.
"""


def main():
    """
    Perform secure file operations using context managers.
    """
    with open("vault.txt", "w") as setup_file:
        setup_file.write("[CLASSIFIED] Quantum encryption keys recovered")

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("SECURE EXTRACTION:")
    try:
        with open("vault.txt", "r") as file:
            content = file.read()
            print(content)
            print("[CLASSIFIED] Archive integrity: 100%")
    except FileNotFoundError:
        print("Error: Vault not found.")

    print("SECURE PRESERVATION:")
    with open("vault.txt", "a") as file:
        file.write("\n[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
