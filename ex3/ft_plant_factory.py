#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, start_height: float, start_age: int) -> None:
        self.name: str = name
        self.start_height: float = start_height
        self.start_age: int = start_age

    def show(self) -> str:
        return f"{self.name}: {self.start_height}cm, {self.start_age} \
days old"

    def grow(self, growth: float) -> float:
        self.height = round(self.start_height + growth, 1)
        return self.height

    def age(self) -> int:
        self.start_age += 1
        return self.start_age


def main() -> None:
    print("=== Plant Factory Output ===")
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
