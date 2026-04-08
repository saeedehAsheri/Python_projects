"""
Spell ingredient validation module.
"""


def validate_ingredients(ingredients: str) -> str:
    """
    Checks if ingredients contain valid elemental components.
    """
    valid_elements = ["fire", "water", "earth", "air"]
    ingredients_lower = ingredients.lower()
    is_valid = any(el in ingredients_lower for el in valid_elements)

    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
