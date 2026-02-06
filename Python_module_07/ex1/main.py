from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    """Demonstrates the Deck Builder system and Polymorphism."""
    print("=== DataDeck Deck Builder ===")
    deck = Deck()

    # Add various card types to the deck
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "Damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana/turn"))

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        if card:
            # Extract card type from class name for display
            c_type = card.__class__.__name__.replace('Card', '')
            print(f"Drew: {card.name} ({c_type})")
            print(f"Play result: {card.play({})}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
        )


if __name__ == "__main__":
    main()
