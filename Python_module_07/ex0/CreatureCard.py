from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    """
    Concrete implementation of a Creature Card.
    Adds attack and health logic to the Card foundation.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implements summoning logic for creatures."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> Dict[str, Any]:
        """Extends base info with creature-specific stats."""
        info = super().get_card_info()
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        })
        return info

    def attack_target(self, target: Any) -> Dict[str, Any]:
        """Executes an attack against another card or entity."""
        target_name = getattr(target, 'name', 'Unknown')
        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
