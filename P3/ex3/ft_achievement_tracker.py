#!/usr/bin/env python3


import random

ALL_ACHIEVEMENTS: list[str] = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable',
    'Speed Runner', 'Survivor', 'Treasure Hunter', 'First Steps',
    'Sharp Mind', 'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 9)
    selected = random.sample(ALL_ACHIEVEMENTS, count)
    return set(selected)


def play_generator() -> tuple[set[str], set[str], set[str], set[str]]:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    return alice, bob, charlie, dylan


def main() -> None:
    alice, bob, charlie, dylan = play_generator()
    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")

    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}")

    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))

    print(f"\nOnly Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    all_set = set(ALL_ACHIEVEMENTS)
    alice_missing = all_set.difference(alice)
    bob_missing = all_set.difference(bob)
    charlie_missing = all_set.difference(charlie)
    dylan_missing = all_set.difference(dylan)

    print(f"\nAlice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
