import random
from typing import List, Dict, Any, Optional
from ex0.Card import Card


class Deck:
    """
    Manages a collection of Card objects.
    Handles adding, removing, shuffling, and drawing cards.
    """

    def __init__(self) -> None:
        """Initializes an empty list of cards."""
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Adds a card instance to the deck."""
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Removes a card by name. Returns True if successful, else False."""
        for card in self._cards:
            if card.name == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomizes the order of the cards in-place."""
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        """Removes and returns the top card from the deck."""
        return self._cards.pop() if self._cards else None

    def get_deck_stats(self) -> Dict[str, Any]:
        """Calculates and returns statistics about the deck composition."""
        if not self._cards:
            return {'total_cards': 0}

        total_cost = sum(card.cost for card in self._cards)
        stats = {
            'total_cards': len(self._cards),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': total_cost / len(self._cards)
        }

        for card in self._cards:
            # Using __class__.__name__ to identify the type of card
            class_name = card.__class__.__name__
            if class_name == 'CreatureCard':
                stats['creatures'] += 1
            elif class_name == 'SpellCard':
                stats['spells'] += 1
            elif class_name == 'ArtifactCard':
                stats['artifacts'] += 1

        return stats
