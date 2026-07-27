#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display(self) -> str:
            return f"Stats: {self.grow_calls} grow, {self.age_calls} age, \
{self.show_calls} show"

    def __init__(self, name: str, start_height: float, start_age: int) -> None:
        self.name: str = name
        self._height: float = start_height
        self._age: int = start_age
        self._stats: Plant.Stats = Plant.Stats()

    def show(self) -> str:
        self._stats.show_calls += 1
        return f"{self.name}: {self._height}cm, {self._age} days old"

    def grow(self, growth: float) -> float:
        self._stats.grow_calls += 1
        self._height = round(self._height + growth, 1)
        self._age += 1
        return self._height

    def age(self) -> None:
        self._stats.age_calls += 1
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

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
        bloom_status = (
            f" {self.name} is blooming beautifully!"
            if self._is_bloomed
            else f" {self.name} has not bloomed yet"
        )
        return f"{base_info}\n  Color: {self.color}\n{bloom_status}"


class Seed(Flower):
    def __init__(self, name: str, start_height: float, start_age: int,
                 color: str) -> None:
        super().__init__(name, start_height, start_age, color)

    def show(self) -> str:
        base_info = super().show()
        seeds_count = 42 if self._is_bloomed else 0
        return f"{base_info}\n  Seeds: {seeds_count}"


class Tree(Plant):
    def __init__(self, name: str, start_height: float, start_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, start_height, start_age)
        self.trunk_diameter: float = trunk_diameter
        self.shade_calls: int = 0

    def produce_shade(self) -> None:
        self.shade_calls += 1
        print(f" Tree {self.name} now produces a shade of {self.get_height()} \
cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> str:
        base_info = super().show()
        return f"{base_info}\n  Trunk diameter: {self.trunk_diameter}cm"


def display_plant_analytics(plant: Plant) -> None:
    print(plant.get_stats().display())
    if isinstance(plant, Tree):
        print(f"  {plant.shade_calls} shade")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    print(" [statistics for Rose]")
    display_plant_analytics(rose)
    print(" [asking the rose to grow and bloom]")
    rose.grow(0.8)
    rose.bloom()
    print(rose.show())
    print("[statistics for Rose]")
    display_plant_analytics(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    print("[statistics for Oak]")
    display_plant_analytics(oak)
    print(" [asking the oak to produce shade]")
    oak.produce_shade()
    print(" [statistics for Oak]")
    display_plant_analytics(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print(sunflower.show())
    print(" [make sunflower grow, age and bloom]")
    sunflower.grow(0.8)
    sunflower.age()
    setattr(sunflower, '_height', 110.0)
    setattr(sunflower, '_age', 65)
    sunflower.bloom()
    print(sunflower.show())
    print(" [statistics for Sunflower]")
    display_plant_analytics(sunflower)
    print("\n=== Anonymous")
    anon_plant = Plant.create_anonymous()
    print(anon_plant.show())
    print(" [statistics for Unknown plant]")
    display_plant_analytics(anon_plant)


if __name__ == "__main__":
    main()
