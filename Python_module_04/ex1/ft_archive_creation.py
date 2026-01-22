"""
Docstring for ex1.ft_archive_creation.
"""


def main():
    """
    Create a new archive file and write preservation entries.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...")

    try:
        file = open("new_discovery.txt", "w")

        print("\nInscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 003] Archived by Data Archivist trainee")

        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

        file.close()

    except Exception as e:
        print(f"Error accessing archive: {e}")


if __name__ == "__main__":
    main()
