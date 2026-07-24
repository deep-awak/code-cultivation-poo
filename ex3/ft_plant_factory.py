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
    rose: Plant = Plant("Rose", 25.0, 30)
    oak: Plant = Plant("Oak", 200.0, 365)
    cactus: Plant = Plant("Cactus", 5.0, 90)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    fern: Plant = Plant("Fern", 15.0, 120)
    list_flower: list[Plant] = [rose, oak, cactus, sunflower, fern]
    for flower in list_flower:
        print(f"Created: {flower.show()}")


if __name__ == "__main__":
    main()
