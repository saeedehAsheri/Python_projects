"""
Docstring for ft_inventory_system
"""
import sys


def insertion_sort(dict_args):
    """
    Sorts a dictionary by value (descending) using a selection approach.
    """
    sorted_dict = dict()

    while len(sorted_dict) < len(dict_args):
        max_val = None
        max_key = None

        for key, value in dict_args.items():
            if sorted_dict.get(key) is not None:
                continue

            if max_key is None:
                max_key = key
                max_val = value
            else:
                if value > max_val:
                    max_val = value
                    max_key = key
        sorted_dict.update({max_key: max_val})
    return sorted_dict


def p_least_most(my_dict):
    """
    Prints the most and least abundant items.
    """
    for key, val in my_dict.items():
        unit_str = "unit" if val == 1 else "units"
        print(f"Most abundant: {key} ({val} {unit_str})")
        break

    last_key = None
    last_val = None
    for key, val in my_dict.items():
        last_key = key
        last_val = val

    if last_key is not None:
        unit_str = "unit" if last_val == 1 else "units"
        print(f"Least abundant: {last_key} ({last_val} {unit_str})")


def make_categories(sorted_dict):
    """
    Categorizes items into Scarce, Moderate, and Abundant.
    """
    scarce = dict()
    moderate = dict()
    abundant = dict()

    for key, val in sorted_dict.items():
        if val < 5:
            scarce.update({key: val})
        elif val >= 5 and val <= 10:
            moderate.update({key: val})
        else:
            abundant.update({key: val})

    if len(abundant) > 0:
        print(f"Abundant: {abundant}")
    if len(moderate) > 0:
        print(f"Moderate: {moderate}")
    if len(scarce) > 0:
        print(f"Scarce: {scarce}")


def show_properties(my_dict):
    """
    Displays the keys and values of the dictionary as lists.
    """
    dict_keys = []
    dict_vals = []
    for key, val in my_dict.items():
        dict_keys += [key]
        dict_vals += [val]

    print(f"Dictionary keys: {dict_keys}")
    print(f"Dictionary values: {dict_vals}")


def lookup(sorted_dict, sample):
    """
    Checks if a specific key exists in the dictionary.
    """
    for k in sorted_dict.keys():
        if k == sample:
            return True
    return False


def main():
    """
    Main function to analyze inventory from command line arguments.
    """
    args = sys.argv
    dict_args = dict()
    if len(args) > 1:
        for arg in args[1:]:
            dic_item = arg.split(':')
            dict_args[dic_item[0]] = int(dic_item[1])

    print("=== Inventory System Analysis ===")
    total_items = 0
    for val in dict_args.values():
        total_items += val
    print(f"Total items in inventory: {total_items}")
    unique_types = len(dict_args)
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    sorted_dict = insertion_sort(dict_args)

    for key, value in sorted_dict.items():
        percent = (value / total_items) * 100
        u_str = "unit" if value == 1 else "units"
        print(f"{key}: {value} {u_str} ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    p_least_most(sorted_dict)

    print("\n=== Item Categories ===")
    make_categories(sorted_dict)

    print("\n=== Management Suggestions ===")
    restock = []
    for key, val in sorted_dict.items():
        if val < 2:
            restock += [key]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    show_properties(dict_args)
    sample = "sword"
    print(f"Sample lookup -'{sample}' in inventory: "
          f"{lookup(sorted_dict, sample)}")


if __name__ == "__main__":
    main()
