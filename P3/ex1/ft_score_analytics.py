import sys


def score_analytics() -> list[int]:
    if len(sys.argv) < 2:
        print(
            f"No scores provided. Usage: python3 {sys.argv[0]} <score1>\
 <score2> ..."
        )
        return []

    error_message = ""
    for arg in sys.argv[1:]:
        try:
            int(arg)
        except (ValueError, TypeError):
            error_message += f"Invalid parameter: '{arg}'\n"

    if error_message:
        error_message += f"No scores provided. Usage: python3 {sys.argv[0]} \
<score1> <score2> ..."
        raise ValueError(error_message)

    return [int(arg) for arg in sys.argv[1:]]


def display_analytics(
    scores: list[int],
    total_players: int,
    total_score: int,
    average_score: float,
    high_score: int,
    low_score: int,
    score_range: int,
) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main() -> None:
    print("=== Player Score Analytics ===")

    try:
        scores: list[int] = score_analytics()
        if not scores:
            return
    except ValueError as error:
        print(error)
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: float = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    display_analytics(
        scores,
        total_players,
        total_score,
        average_score,
        high_score,
        low_score,
        score_range,
    )


if __name__ == "__main__":
    main()
