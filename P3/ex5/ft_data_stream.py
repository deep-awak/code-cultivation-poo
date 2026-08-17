#!/usr/bin/env python3

import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab",
           "move", "climb", "swim", "release", "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while event_list:
        index = random.randrange(len(event_list))
        event = event_list.pop(index)
        yield event


def stream_thousand_events(stream:
                           Generator[tuple[str, str], None, None]) -> None:
    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")


def generate_event_batch(
    stream: Generator[tuple[str, str], None, None], count: int
) -> list[tuple[str, str]]:
    """Generates a list of N events using next() on the stream generator."""
    events: list[tuple[str, str]] = []
    for _ in range(count):
        events += [next(stream)]
    return events


def process_event_consumption(event_list: list[tuple[str, str]]) -> None:
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    stream_thousand_events(stream)

    event_list = generate_event_batch(stream, 10)
    print(f"Built list of 10 events: {event_list}")

    process_event_consumption(event_list)


if __name__ == "__main__":
    main()
