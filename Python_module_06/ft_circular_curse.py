"""
Demonstration script for breaking circular dependencies.
"""
from alchemy.grimoire import validate_ingredients, record_spell


def main():
    """
    Executes tests for circular curse breaking.
    """
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
