def game_event_generator(total_events):
    """
    Generate a stream of game events using a pattern.

    This function simulates game data without using random libraries.
    It yields data one by one to save memory.

    Args:
        total_events (int): The total number of events to generate.

    Yields:
        tuple: A tuple containing (player_name, level, action_type).
    """
    names = ["alice", "bob", "charlie", "dave", "eve"]
    actions = ["killed monster", "found treasure", "leveled up", "died"]

    n_names = len(names)
    n_actions = len(actions)

    for i in range(total_events):
        name = names[i % n_names]

        level = (i % 20) + 1

        action = actions[i % n_actions]

        yield (name, level, action)


def fibonacci_generator():
    """
    Generate an infinite sequence of Fibonacci numbers.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    """
    Generate an infinite sequence of Prime numbers.

    This function checks for primality using a loop and yields
    the number if it is prime.

    Yields:
        int: The next prime number.
    """
    num = 2
    while True:
        is_prime = True
        if num > 1:
            limit = int(num ** 0.5) + 1
            for i in range(2, limit):
                if num % i == 0:
                    is_prime = False
                    break

        if is_prime:
            yield num

        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...")

    count_high_level = 0
    count_treasure = 0
    count_level_up = 0

    stream = game_event_generator(total_events)

    i = 0
    for event_data in stream:
        i += 1
        name, level, action = event_data

        if i <= 3:
            print(f"Event {i}: Player {name} (level {level}) {action}")
        elif i == 4:
            print("...")

        if level >= 10:
            count_high_level += 1

        if action == "found treasure":
            count_treasure += 1
        elif action == "leveled up":
            count_level_up += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {count_high_level}")
    print(f"Treasure events: {count_treasure}")
    print(f"Level-up events: {count_level_up}")
    print("Memory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")

    fib_gen = fibonacci_generator()
    fib_list = []
    for _ in range(10):
        fib_list.append(str(next(fib_gen)))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_gen = prime_generator()
    prime_list = []
    for _ in range(5):
        prime_list.append(str(next(prime_gen)))
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")
