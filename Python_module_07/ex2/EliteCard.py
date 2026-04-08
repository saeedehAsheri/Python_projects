from typing import Dict, Any, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    A powerful card type that combines physical combat and magic.
    Implements multiple inheritance from Card, Combatable, and Magical.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, mana_capacity: int):
        """Initializes the elite card with both combat and magic stats."""
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack_power
        self.mana: int = mana_capacity

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implements the required play method from Card."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'status': 'Elite Card deployed with combat and magic ready'
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        target_name = getattr(target, 'name', 'Enemy')
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = 3
        taken = max(0, incoming_damage - blocked)
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': True
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {'attack_power': self.attack_power}

    def cast_spell(
            self, spell_name: str, targets: List[Any]
            ) -> Dict[str, Any]:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [getattr(t, 'name', str(t)) for t in targets],
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> Dict[str, Any]:
        return {'mana_capacity': self.mana}
