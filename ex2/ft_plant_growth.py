#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self._age} days old"

    def grow(self) -> float:
        self.height = round(self.height + 0.8, 1)
        return self.height

    def age(self) -> int:
        self._age += 1
        return self._age


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    init_height = rose.height
    print("=== Garden Plant Growth ===")
    print(rose.show())

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        print(rose.show())

    total_height = rose.height
    print(f"Growth this week: {round(total_height - init_height, 1)}cm")


if __name__ == "__main__":
    main()
