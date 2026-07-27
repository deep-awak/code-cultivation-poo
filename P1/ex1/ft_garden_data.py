#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    sunflower = Plant("Sunflower", 80.0, 45)
    cactus = Plant("Cactus", 15.0, 120)
    print("=== Garden Plan Registry ===")
    print(f"{rose.show()}\n{sunflower.show()}\n{cactus.show()}")


if __name__ == "__main__":
    main()
