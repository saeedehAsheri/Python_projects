from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract interface for entities that can be ranked."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculates and returns the current performance rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Increments the win count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Increments the loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict[str, int]:
        """Returns a summary of wins, losses, and rating."""
        pass
