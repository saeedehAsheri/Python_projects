from typing import Dict, Any, Union, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory for fantasy-themed cards."""

    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Creates Dragons or Goblins based on input."""
        if name_or_power == "dragon" or (
            isinstance(name_or_power, int) and name_or_power > 5
        ):
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Creates a Fireball/Lightning Bolt spell."""
        return SpellCard("Lightning Bolt", 3, "Common", "Damage")

    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Creates magical artifacts like Rings."""
        return ArtifactCard("Mana Ring", 2, "Rare", 3, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Returns metadata for a themed deck."""
        return {"deck_size": size, "theme": "Fantasy"}

    def get_supported_types(self) -> Dict[str, Any]:
        """Returns dictionary of supported fantasy types."""
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
