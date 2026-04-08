from ex2.EliteCard import EliteCard


def main() -> None:
    """Demonstrates multiple inheritance and interface design."""
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    warrior = EliteCard("Arcane Warrior", 6, "Epic", 5, 4)
    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(
        f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
        )
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
