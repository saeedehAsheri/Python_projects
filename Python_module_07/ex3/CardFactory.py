from abc import ABC, abstractmethod
from typing import Dict, Any, Union, Optional
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract interface for creating themed cards."""

    @abstractmethod
    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Creates a themed creature card."""
        pass

    @abstractmethod
    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Creates a themed spell card."""
        pass

    @abstractmethod
    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Creates a themed artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Generates a full deck of themed cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, Any]:
        """Returns types of cards this factory can produce."""
        pass
