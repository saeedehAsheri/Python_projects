from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """
    Create a counting closure that increments on each call.

    :return: A function that returns the current count.
    :rtype: Callable[[], int]
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Create a power accumulator starting from an initial value.

    :param initial_power: The starting power level.
    :type initial_power: int
    :return: A function that adds power and returns the new total.
    :rtype: Callable[[int], int]
    """
    power_i = initial_power

    def accumulate(amount: int) -> int:
        nonlocal power_i
        try:
            power_i += amount
        except TypeError:
            print("Error: Power amount must be an integer.")
            return power_i
        return power_i
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Generate functions that apply a specific enchantment prefix to items.

    :param enchantment_type: The type of enchantment (e.g., 'Flaming').
    :type enchantment_type: str
    :return: A function that enchant items.
    :rtype: Callable[[str], str]
    """
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> Dict[str, Callable]:
    """
    Create a private memory storage accessible via store and recall functions.

    :return: A dictionary containing 'store' and 'recall' closures.
    :rtype: Dict[str, Callable]
    """
    vault = {}

    def store(key: str, val: Any) -> None:
        try:
            vault[key] = val
        except Exception as e:
            print(f"Failed to store memory: {e}")

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    try:
        print("\nTesting mage counter...")
        mage_c = mage_counter()
        print(f"Call 1: {mage_c()}")
        print(f"Call 2: {mage_c()}")
        print(f"Call 3: {mage_c()}")

        print("\nTesting spell_accumulator...")
        acc = spell_accumulator(100)
        print(f"Initial 100, add 50: {acc(50)}")
        print(f"Add another 25: {acc(25)}")

        print("\nTesting enchantment factory...")
        enchantment1 = enchantment_factory("Flaming")
        print(enchantment1("Sword"))
        enchantment2 = enchantment_factory("Frozen")
        print(enchantment2("Shield"))

        print("\nTesting memory_vault...")
        vault_functions = memory_vault()
        vault_functions["store"]("secret_spell", "Abracadabra")
        print(f"Recalling 'secret_spell': {vault_functions['recall']('secret_spell')}")  # noqa: E501
        print(f"Recalling 'missing': {vault_functions['recall']('missing')}")

    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")


if __name__ == "__main__":
    main()
