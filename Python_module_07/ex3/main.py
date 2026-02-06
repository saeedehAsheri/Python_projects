from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Main execution point for testing the Game Engine."""
    print("=== DataDeck Game Engine ===")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")

    turn_exec = engine.simulate_turn()
    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_exec}")

    print("\nGame Report:")
    print(engine.get_engine_status())
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
        )


if __name__ == "__main__":
    main()
