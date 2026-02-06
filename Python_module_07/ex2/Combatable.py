from abc import ABC, abstractmethod
from typing import Dict, Any


class Combatable(ABC):
    """Abstract interface for cards capable of physical combat."""

    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        """Perform a physical attack."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Process incoming damage and mitigate it."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """Return statistics related to combat abilities."""
        pass
