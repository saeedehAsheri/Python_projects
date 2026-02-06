from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demonstrates the DataDeck Card Foundation."""
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 1, "Common", 1, 1)

        print("\nCreatureCard Info:")
        print(dragon.get_card_info())

        mana = 6
        print(f"\nPlaying {dragon.name} with {mana} mana available:")
        print(f"Playable: {dragon.is_playable(mana)}")
        print(f"Play result: {dragon.play({})}")

        print(f"\n{dragon.name} attacks {goblin.name}:")
        print(f"Attack result: {dragon.attack_target(goblin)}")

        mana_low = 3
        print(f"\nTesting insufficient mana ({mana_low} available):")
        print(f"Playable: {dragon.is_playable(mana_low)}")

        print("\nAbstract pattern successfully demonstrated!")

    except Exception as e:
        print(f"An error occurred during execution: {e}")


if __name__ == "__main__":
    main()
