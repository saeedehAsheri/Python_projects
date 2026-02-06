from typing import List, Dict, Any
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete strategy focusing on low-cost cards and direct damage."""

    def get_strategy_name(self) -> str:
        """Returns the name of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Targets the enemy player as top priority."""
        if "Enemy Player" in available_targets:
            others = [t for t in available_targets if t != "Enemy Player"]
            return ["Enemy Player"] + others
        return available_targets

    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Executes an aggressive turn logic."""
        # Sort hand by cost (low to high) to play more cards quickly
        playable_cards = sorted(hand, key=lambda x: x.cost)
        played = [card.name for card in playable_cards]
        total_mana = sum(card.cost for card in playable_cards)

        return {
            'cards_played': played,
            'mana_used': total_mana,
            'targets_attacked': self.prioritize_targets(["Enemy Player"]),
            'damage_dealt': 8
        }
