"""
Game Analytics Dashboard.

This script demonstrates how to use Python comprehensions (List, Dict, Set)
to analyze game data. It filters players, calculates scores, and finds
unique achievements.
"""


def main():
    game_data = [
        {
            "player": "alice",
            "score": 2300,
            "achievements": ["first_blood", "master"],
            "region": "north",
            "active": 1
        },
        {
            "player": "bob",
            "score": 1800,
            "achievements": ["healer"],
            "region": "east",
            "active": 1
        },
        {
            "player": "charlie",
            "score": 2150,
            "achievements": ["sharpshooter", "master"],
            "region": "north",
            "active": 1
        },
        {
            "player": "diana",
            "score": 2050,
            "achievements": ["runner"],
            "region": "west",
            "active": 0
        },
        {
            "player": "evan",
            "score": 1500,
            "achievements": ["healer", "helper"],
            "region": "east",
            "active": 0
        },
        {
            "player": "frank",
            "score": 1200,
            "achievements": [],
            "region": "south",
            "active": 0
        },
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p["player"] for p in game_data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [p["score"] * 2 for p in game_data]
    print(f"Scores doubled: {doubled_scores}")

    all_players_list = [p["player"] for p in game_data if p["active"] == 1]
    print(f"Active players list: {all_players_list}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p["player"]: p["score"] for p in game_data}
    print(f"Player scores: {player_scores}")

    all_categories = [
        "high" if p["score"] > 2000 else (
            "medium" if p["score"] >= 1500 else "low"
        )
        for p in game_data
    ]

    cats_to_count = ["high", "medium", "low"]
    score_cat = {
        cat: len([x for x in all_categories if x == cat])
        for cat in cats_to_count
    }
    print(f"Score categories: {score_cat}")

    achievement_counts = {
        p["player"]: len(p["achievements"]) for p in game_data
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["player"] for p in game_data}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for p in game_data for ach in p["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["region"] for p in game_data if p["active"] == 1}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(game_data)
    total_unique_achievements = len(unique_achievements)
    avg_score = sum([p["score"] for p in game_data]) / len(game_data)
    top_performer = max(game_data, key=lambda x: x["score"])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_performer['player']} "
          f"({top_performer['score']} points, "
          f"{len(top_performer['achievements'])} achievements)")


if __name__ == "__main__":
    main()
