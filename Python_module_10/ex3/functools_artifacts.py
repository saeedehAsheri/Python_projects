import functools
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the given operation."""
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    try:
        return functools.reduce(operations[operation], spells)
    except (KeyError, TypeError):
        print("Error: invalid operation or spell list.")
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create specialized enchantment functions using partial."""
    fire_enchant = functools.partial(base_enchantment, 50, "fire")
    ice_enchant = functools.partial(base_enchantment, 50, "ice")
    lightning_enchant = functools.partial(base_enchantment, 50, "lightning")

    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Create a single-dispatch spell system."""
    @functools.singledispatch
    def dispatcher(spell: Any) -> None:
        print(f"Unknown spell type: {type(spell).__name__}")

    @dispatcher.register
    def _(spell: int) -> None:
        print(f"Casting Damage Spell: -{spell} HP to enemy!")

    @dispatcher.register
    def _(spell: str) -> None:
        print(f"Casting Enchantment: {spell} applied!")

    @dispatcher.register
    def _(spell: list) -> None:
        print(f"Multi-casting sequence of {len(spell)} spells!")

    return dispatcher


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {element} (Power: {power})"


def main() -> None:
    spells = [20, 30, 40, 10]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire_enchant"]("Sword"))
    print(enchanters["ice_enchant"]("Shield"))
    print(enchanters["lightning_enchant"]("Hammer"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    dispatcher(150)
    dispatcher("Flaming Weapon")
    dispatcher(["fireball", "heal", "shield"])


if __name__ == "__main__":
    main()
