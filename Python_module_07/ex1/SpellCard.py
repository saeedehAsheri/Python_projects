from typing import Dict, Any, List
from ex0.Card import Card


class SpellCard(Card):
    """
    Concrete implementation of a Spell Card.
    Represents instant magical effects that are consumed after use.
    """

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Initializes a SpellCard with a specific effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Triggers the spell effect and returns the action result."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Instant {self.effect_type} effect triggered'
        }

    def resolve_effect(self, targets: List[Any]) -> Dict[str, Any]:
        """Resolves the specific mechanics of the spell on given targets."""
        return {
            'spell': self.name,
            'type': self.effect_type,
            'targets_affected': len(targets),
            'status': 'Resolved'
        }
