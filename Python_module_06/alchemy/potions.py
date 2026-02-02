"""
Advanced potion recipe modules.
"""
from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """
    Brews a healing potion.
    """
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """
    Brews a strength potion.
    """
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """
    Brews an invisibility potion.
    """
    return (f"Invisibility potion brewed with {create_air()} and "
            f"{create_water()}")


def wisdom_potion() -> str:
    """
    Brews a wisdom potion using all elements.
    """
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    return (f"Wisdom potion brewed with all elements: {fire}, {water}, "
            f"{earth}, {air}")
