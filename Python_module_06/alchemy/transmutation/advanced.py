"""
Advanced transmutation spells.
"""
from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    Creates a philosopher's stone.
    """
    return (f"Philosopher’s stone created using {lead_to_gold()} and "
            f"{healing_potion()}")


def elixir_of_life() -> str:
    """
    Creates the elixir of life.
    """
    return "Elixir of life: eternal youth achieved!"
