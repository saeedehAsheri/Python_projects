from typing import Callable, Any, List, Tuple


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combine two spell functions into a single function.
    The new function returns a tuple containing results from both spells.
    """
    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        try:
            return (spell1(*args, **kwargs), spell2(*args, **kwargs))
        except Exception as e:
            return (f"Error in spell1: {e}", f"Error in spell2: {e}")
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplify the numerical result of a base spell by a given multiplier.
    """
    def amplified(*args: Any, **kwargs: Any) -> Any:
        try:
            result = base_spell(*args, **kwargs)
            return result * multiplier
        except (TypeError, ValueError) as e:
            return f"Amplification failed: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Return a function that only executes the spell if the condition is True.
    """
    def validated_cast(*args: Any, **kwargs: Any) -> Any:
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        except Exception as e:
            return f"Condition check failed: {e}"
    return validated_cast


def spell_sequence(spells: List[Callable]) -> Callable:
    """
    Create a sequence of spells to be executed in order.
    Returns a function that collects all spell results into a list.
    """
    def sequence(*args: Any, **kwargs: Any) -> List[Any]:
        results = []
        for s in spells:
            try:
                results.append(s(*args, **kwargs))
            except Exception as e:
                results.append(f"Spell in sequence failed: {e}")
        return results
    return sequence


def fireball(target: str) -> str:
    """Return a fireball strike string."""
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    """Return a healing spell string."""
    return f"Heals {target}"


def base_damage(target: str) -> int:
    """Return base damage as an integer."""
    return 10


def is_dragon(target: str) -> bool:
    """Check if the target is a dragon."""
    return target.lower() == "dragon"


def main():
    """Run test cases for Higher-Order Functions."""
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined('Dragon'))}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(base_damage, 3)
    print(f"Original: {base_damage('Dragon')}, "
          f"Amplified: {mega_fireball('Dragon')}")

    print("\nTesting conditional caster...")
    dragon_slayer = conditional_caster(is_dragon, fireball)
    print(f"Targeting Dragon: {dragon_slayer('Dragon')}")
    print(f"Targeting Orc: {dragon_slayer('Orc')}")

    print("\nTesting spell sequence...")
    magic_combo = spell_sequence([fireball, heal, fireball])
    results = magic_combo('Hydra')
    print(f"Sequence results: {', '.join(results)}")


if __name__ == "__main__":
    main()
