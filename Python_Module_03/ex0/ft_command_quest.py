import sys

print("=== Command Quest ===")

args = sys.argv
total_args = len(args)

if total_args == 1:
    print("No arguments provided!")
    print(f"Program name: {args[0]}")
    print(f"Total arguments: 1")
else:
    print(f"Program name: {args[0]}")
    
    args_received = total_args - 1
    print(f"Arguments received: {args_received}")
    
    for i in range(1, total_args):
        print(f"Argument {i}: {args[i]}")
        
    print(f"Total arguments: {total_args}")
