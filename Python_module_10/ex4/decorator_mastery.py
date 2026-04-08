import functools
import time
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints function execution time."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power levels for spells."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(
            self, spell_name: str, power: int, *args: Any, **kwargs: Any
        ) -> Any:
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries a function if it raises an exception."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Mage guild utilities and spell casting methods."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name has at least 3 letters/spaces only."""
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if the power level is sufficient."""
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Simulate a timed spell."""
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    """Simulate a spell that always fails."""
    raise ValueError("Magic failure")


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    print("\nTesting retry spell...")
    print(unstable_spell())


if __name__ == "__main__":
    main()
