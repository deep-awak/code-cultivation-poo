from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulate(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> dict[str, Callable[..., Any]]:
    storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    c1 = mage_counter()
    c2 = mage_counter()
    print(c1())
    print(c1())
    print(c2())

    acc = spell_accumulator(100)
    print(acc(20))
    print(acc(30))

    flaming = enchantment_factory("Flaming")
    print(flaming("Sword"))

    vault = memory_vault()
    vault["store"]("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))
