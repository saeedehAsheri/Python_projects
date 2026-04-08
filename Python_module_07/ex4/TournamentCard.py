from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card class that implements combat and ranking capabilities."""

    def __init__(self, card_id: str, name: str, cost: int, rarity: str):
        """Initializes a card with tournament-specific tracking."""
        super().__init__(name, cost, rarity)
        self.card_id: str = card_id
        self._wins: int = 0
        self._losses: int = 0
        self._rating: int = 1200

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implements the play method from Card."""
        return {'action': 'played', 'card': self.name}

    def attack(self, target: Any) -> Dict[str, Any]:
        """Implements the attack method from Combatable."""
        return {'attacker': self.name, 'damage': 5}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Implements the defend method from Combatable."""
        return {'defender': self.name, 'absorbed': 2}

    def get_combat_stats(self) -> Dict[str, Any]:
        """Returns combat-related statistics."""
        return {'power': 5}

    def calculate_rating(self) -> int:
        """Returns the current Elo-like rating."""
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Updates win count and increases rating."""
        self._wins += wins
        self._rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        """Updates loss count and decreases rating."""
        self._losses += losses
        self._rating -= (losses * 16)

    def get_rank_info(self) -> Dict[str, int]:
        """Returns a summary of ranking data."""
        return {
            'wins': self._wins,
            'losses': self._losses,
            'rating': self._rating
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        """Returns comprehensive tournament performance data."""
        return {
            'id': self.card_id,
            'name': self.name,
            'record': f"{self._wins}-{self._losses}",
            'rating': self._rating
        }
