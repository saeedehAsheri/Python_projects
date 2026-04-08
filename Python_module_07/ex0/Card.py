from abc import ABC, abstractmethod
from typing import Dict, Any


class Card(ABC):
    """
    Abstract Base Class for all cards in DataDeck.
    Defines the universal contract for card behavior.
    """

    def __init__(self, name: str, cost: int, rarity: str):
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Abstract method to play the card.
        Must be implemented by children."""
        pass

    def get_card_info(self) -> Dict[str, Any]:
        """Returns a dictionary containing the card's basic attributes."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Returns True if the card cost is less than or equal to mana."""
        return available_mana >= self.cost
