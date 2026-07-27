#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, start_height: float, start_age: int) -> None:
        self.name: str = name
        self._height: float = start_height
        self._age: int = start_age

    def show(self) -> str:
        return f"{self.name}: {self._height}cm, {self._age} days old"

    def grow(self, growth: float) -> float:
        self._height = round(self._height + growth, 1)
        return self._height

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def _is_invalid(self, value: float, field: str) -> bool:
        if value < 0:
            print(f"{self.name}: Error, {field} can't be negative\n \
{field.capitalize()} update rejected")
        return value < 0

    def set_height(self, new_height: float) -> None:
        if not self._is_invalid(new_height, "height"):
            self._height = round(float(new_height), 1)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if not self._is_invalid(new_age, "age"):
            self._age = new_age
            print(f"Age updated: {self._age} days")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-1)
    rose.set_age(-10)
    print(f"\nCurrent state: {rose.show()}")


if __name__ == "__main__":
    main()
