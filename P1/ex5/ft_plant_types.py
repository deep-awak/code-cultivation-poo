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
        self._age += 1
        return self._height

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def _validate_positive(self, value: float, field_name: str) -> bool:
        if value < 0:
            print(f"{self.name}: Error, {field_name} can't be negative")
            print(f"{field_name.capitalize()} update rejected")
            return False
        return True

    def set_height(self, new_height: float) -> None:
        if self._validate_positive(new_height, "height"):
            self._height = round(float(new_height), 1)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if self._validate_positive(new_age, "age"):
            self._age = new_age
            print(f"Age updated: {self._age} days")


class Flower(Plant):
    def __init__(self, name: str, start_height: float, start_age: int,
                 color: str) -> None:
        super().__init__(name, start_height, start_age)
        self.color: str = color
        self._is_bloomed: bool = False

    def bloom(self) -> None:
        self._is_bloomed = True

    def show(self) -> str:
        base_info = super().show()
        bloom_status = f" {self.name} is blooming beautifully!"\
            if self._is_bloomed else f" {self.name} has not bloomed yet"
        return f"{base_info}\n Color: {self.color}\n{bloom_status}"


class Tree(Plant):
    def __init__(self, name: str, start_height: float, start_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, start_height, start_age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.get_height()}\
cm long and {self.trunk_diameter}cm wide.\n")

    def show(self) -> str:
        base_info = super().show()
        return f"{base_info}\n Trunk diameter: {self.trunk_diameter}cm"


class Vegetable(Plant):
    def __init__(self, name: str, start_height: float, start_age: int,
                 harvest_season: str) -> None:
        super().__init__(name, start_height, start_age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, growth: float) -> float:
        new_height = super().grow(growth)
        self.nutritional_value += 1
        return new_height

    def show(self) -> str:
        base_info = super().show()
        return f"{base_info}\n Harvest season: {self.harvest_season}\
            \n Nutritional value: {self.nutritional_value}"


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    print("[asking the rose to bloom]")
    rose.bloom()
    print(f"{rose.show()}\n")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print(tomato.show())
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(0.8)
    print(tomato.show())


if __name__ == "__main__":
    main()
