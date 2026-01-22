"""
Docstring for ex4.ft_inventory_system
"""
import sys


def main():
    """
    Docstring for main
    """
    args = sys.argv
    dict_args = {}
    if len(args) > 1:
        for arg in args[1:]:
            dic_item = arg.split(':')
            dict_args[dic_item[0]] = int(dic_item[1])

    print("=== Inventory System Analysis ===")
    total_items = sum(dict_args.values())
    print(f"Total items in inventory: {total_items}")
    unique_types = len(dict_args)
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    total_value = 0
    for val in dict_args.values():
        total_value += val

    # Sorting logic to match the expected output (Highest to Lowest)
    sorted_items = sorted(
        dict_args.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for key, value in sorted_items:
        print(f"{key}: {value} units ({(value / total_value) * 100:.1f}%)")

    print("\n=== Inventory Statistics ===")
    # Finding max and min based on values
    most_abundant = max(dict_args, key=dict_args.get)
    least_abundant = min(dict_args, key=dict_args.get)
    print(f"Most abundant: {most_abundant} ({dict_args[most_abundant]} units)")
    print(f"Least abundant: {least_abundant} ({dict_args[least_abundant]} unit)")

    print("\n=== Item Categories ===")
    categories = {
        "Moderate": {},
        "Scarce": {}
    }
    for key, value in dict_args.items():
        if value >= 5:
            categories["Moderate"][key] = value
        else:
            categories["Scarce"][key] = value
    
    # We strip the quotes from the output to match the exercise exactly
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    print("\n=== Management Suggestions ===")
    restock_needed = [key for key, val in dict_args.items() if val < 2]
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(dict_args.keys())}")
    print(f"Dictionary values: {list(dict_args.values())}")
    
    # Sample lookup check
    sample_key = 'sword'
    is_in_inventory = sample_key in dict_args
    print(f"Sample lookup - '{sample_key}' in inventory: {is_in_inventory}")


if __name__ == "__main__":
    main()