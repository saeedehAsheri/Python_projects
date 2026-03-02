from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Sort magical artifacts by power level descending."""
    try:
        return sorted(artifacts, key=lambda x: x["power"], reverse=True)
    except (KeyError, TypeError):
        print("Error: Artifacts must be a list of dicts with 'power' key.")
        return []


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filter mages by power level."""
    try:
        return list(filter(lambda x: x["power"] >= min_power, mages))
    except (KeyError, TypeError):
        print("Error: Mages must be a list of dicts with 'power' key.")
        return []


def spell_transformer(spells: List[str]) -> List[str]:
    """Transform spell names with star prefixes and suffixes."""
    try:
        return list(map(lambda x: f"* {x} *", spells))
    except TypeError:
        print("Error: Input must be a list of strings.")
        return []


def mage_stats(mages: List[Dict]) -> Dict:
    """Calculate max, min, and average power levels of mages."""
    try:
        powers = list(map(lambda m: m['power'], mages))
        max_p = max(powers)
        min_p = min(powers)
        avg_p = round(sum(powers) / len(powers), 2)

        return {
            "max_power": max_p,
            "min_power": min_p,
            "avg_power": avg_p
        }
    except (ValueError, KeyError, ZeroDivisionError):
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}


def main():
    """Main function to demonstrate the magic functions."""
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Magic"},
        {"name": "Fire Staff", "power": 92, "type": "Weapon"},
        {"name": "Old Scroll", "power": 45, "type": "Knowledge"},
        {"name": "Ancient Shield", "power": 70, "type": "Defense"},
        {"name": "Shadow Dagger", "power": 95, "type": "Weapon"}
    ]

    mages = [
        {"name": "Aria the Breeze", "power": 82, "element": "Air"},
        {"name": "Ignis the Bold", "power": 95, "element": "Fire"},
        {"name": "Terra the Rock", "power": 78, "element": "Earth"},
        {"name": "Aqua the Wave", "power": 88, "element": "Water"},
        {"name": "Shadow Night", "power": 65, "element": "Shadow"}
    ]

    spells = ["fireball", "heal", "shield"]

    sorted_art = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    if len(sorted_art) > 1:
        print(f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power) "
              f"comes before {sorted_art[1]['name']} "
              f"({sorted_art[1]['power']} power)")

    print("\nTesting power filter...")
    print(f"Mages with power >= 85: {power_filter(mages, 85)}")

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting mages stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
