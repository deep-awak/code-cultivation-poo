import functools
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError("Unsupported operation")


def partial_enchanter(base_enchantment: Callable[..., str]
                      ) -> dict[str, Callable[..., str]]:
    fire_el = functools.partial(base_enchantment, 50, "fire")
    ice_el = functools.partial(base_enchantment, 50, "ice")
    lightning_el = functools.partial(base_enchantment, 50, "lightning")
    return {
        "fire": fire_el,
        "ice": ice_el,
        "lightning": lightning_el
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


if __name__ == "__main__":
    print(spell_reducer([10, 20, 30], "add"))
    print(spell_reducer([10, 20, 30], "multiply"))
    print(spell_reducer([10, 20, 30], "max"))
    print(spell_reducer([10, 20, 30], "min"))

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Power {power}, Element {element}, Target {target}"

    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Dragon"))

    print(memoized_fibonacci(10))

    disp = spell_dispatcher()
    print(disp(42))
    print(disp("fireball"))
    print(disp([1, 2, 3]))
    print(disp(3.14))
