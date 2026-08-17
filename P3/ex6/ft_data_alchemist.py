#!/usr/bin/env python3

import random

INITIAL_PLAYERS = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def capitalize_all_names(players: list[str]) -> list[str]:
    return [player.capitalize() for player in players]


def filter_capitalized_names(players: list[str]) -> list[str]:
    return [player for player in players if player[0].isupper()]


def generate_scores(players: list[str]) -> dict[str, int]:
    return {player: random.randint(1, 1000) for player in players}


def calculate_average_score(scores: dict[str, int]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores.values()) / len(scores), 2)


def filter_high_scores(
    scores: dict[str, int], average: float
) -> dict[str, int]:
    return {
        player: score for player, score in scores.items() if score > average
    }


def main() -> None:
    print("=== Game Data Alchemist ===")

    print("Initial list of players:", INITIAL_PLAYERS)

    all_capitalized = capitalize_all_names(INITIAL_PLAYERS)
    print("New list with all names capitalized:", all_capitalized)

    capitalized_only = filter_capitalized_names(INITIAL_PLAYERS)
    print("New list of capitalized names only:", capitalized_only)

    score_dict = generate_scores(all_capitalized)
    print("Score dict:", score_dict)

    avg_score = calculate_average_score(score_dict)
    print(f"Score average is {avg_score:.2f}")

    high_scores = filter_high_scores(score_dict, avg_score)
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
