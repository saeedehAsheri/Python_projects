from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):
    """
    Concrete implementation of an Artifact Card.
    Represents permanent modifiers that remain in play.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        """Initializes an ArtifactCard with durability and permanent effect."""
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect_description: str = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Deploys the artifact onto the game field."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect_description}'
        }

    def activate_ability(self) -> Dict[str, Any]:
        """Triggers the artifact's unique ability."""
        return {
            'artifact': self.name,
            'action': 'Ability activated',
            'remaining_durability': self.durability
        }
