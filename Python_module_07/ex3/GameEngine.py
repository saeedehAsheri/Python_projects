from typing import Dict, Any, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrator that combines Factory and Strategy patterns."""

    def __init__(self) -> None:
        """Initializes an empty game engine."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Configures the engine with a specific factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        """Simulates a game turn and updates engine stats."""
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured with factory/strategy!")

        # Generate sample hand
        c1 = self.factory.create_creature("dragon")
        c2 = self.factory.create_creature("goblin")
        s1 = self.factory.create_spell()
        self._cards_created += 3

        hand = [c1, c2, s1]
        turn_result = self.strategy.execute_turn(hand, [])
        self._total_damage += turn_result.get('damage_dealt', 0)

        return turn_result

    def get_engine_status(self) -> Dict[str, Any]:
        """Returns the cumulative game report."""
        strategy_name = (
            self.strategy.get_strategy_name() if self.strategy else None
        )
        return {
            'turns_simulated': 1,
            'strategy_used': strategy_name,
            'total_damage': self._total_damage,
            'cards_created': self._cards_created
        }
