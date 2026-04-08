from abc import ABC, abstractmethod
from typing import List, Dict, Any


class GameStrategy(ABC):
    """Abstract interface for AI game strategies."""

    @abstractmethod
    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Defines how to play cards and attack during a turn."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Returns the identifier for the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Orders targets based on strategy priority."""
        pass
