"""
Command Quest.

This script demonstrates how to read 'arguments' passed to a program from the
terminal. It acts like a gatekeeper that counts and lists whoever enters.
"""
import sys

print("=== Command Quest ===")

args = sys.argv
total_args = len(args)

if total_args == 1:
    print("No arguments provided!")
    print(f"Program name: {args[0]}")
    print("Total arguments: 1")
else:
    print(f"Program name: {args[0]}")

    args_received = total_args - 1
    print(f"Arguments received: {args_received}")

    for i in range(1, total_args):
        print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {total_args}")
