import sys

print("=== Player Score Analytics ===")
args = sys.argv
len_args = len(sys.argv)

if len_args == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    try:
        list_args = []
        for ar in range(1, len_args):
            list_args.append(int(args[ar]))
    
        print(f"Total players: {len_args - 1}")
        print(f"Total score: {sum(list_args)}")
        print(f"Average score: {sum(list_args) / len_args}")
        print(f"High score: {max(list_args)}")
        print(f"Low score: {min(list_args)}")
        print(f"Score range: {max(list_args) - min (list_args)}")
    except ValueError:
        print("Error: All scores must be integer numbers.")

