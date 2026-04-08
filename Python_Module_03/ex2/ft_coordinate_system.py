"""
This program creates a simple 3D coordinate system.
It converts text input into numbers and calculates distances.
"""
import sys
import math


def calculate_distance(p1, p2):
    """
    Calculates the distance between two points in 3D space.

    It uses the standard math formula for distance.
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist


def parsing(pos):
    """
    Converts a text string into a group of three numbers (a tuple).

    If the text is not a valid number or does not have three parts,
    it prints an error message and returns None.
    """
    print(f'Parsing coordinates: "{pos}"')
    try:
        split_pos = pos.split(',')
        if len(split_pos) != 3:
            raise ValueError("Input must have exactly 3 coordinates")
        coords_list = [int(item) for item in split_pos]
        tuple_pos = tuple(coords_list)
        print(f"Parsed position: {tuple_pos}")
        return tuple_pos
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{pos}"')
        print(f"Error parsing coordinates: {e}")
        error_type = type(e).__name__
        print(f"Error details - Type: {error_type}, Args: {e.args}")
        return None


def main():
    """
    The main part of the program that runs the game logic.

    It gets input from the user, processes the coordinates,
    and calculates the distance from the center point (0, 0, 0).
    """
    print("=== Game Coordinate System ===")
    args = sys.argv
    if len(args) < 2:
        user_input = "10,20,5"
    else:
        user_input = args[1]

    origin = (0, 0, 0)
    player_pos = parsing(user_input)

    if player_pos is None:
        return

    print(f"Position created: {player_pos}")
    dist = calculate_distance(player_pos, origin)
    print(f"Distance between {origin} and {player_pos}: {round(dist, 2)}")

    print("\nUnpacking demonstration:")
    x, y, z = player_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
