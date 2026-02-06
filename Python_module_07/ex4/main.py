from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Demonstrates the unified tournament platform functionality."""
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    # Create and register cards
    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary")
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Rare")

    print("Registering Tournament Cards...")
    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in [dragon, wizard]:
        stats = card.get_tournament_stats()
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {stats['rating']}")
        print(f"- Record: {stats['record']}")

    print("\nCreating tournament match...")
    match_res = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_res}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    main()
