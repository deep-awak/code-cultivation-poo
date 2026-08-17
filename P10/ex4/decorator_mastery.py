from collections.abc import Callable
import functools
import time
from typing import Any, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])


def spell_timer(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return cast(F, wrapper)


def power_validator(min_power: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: int | None = None
            if "power" in kwargs and isinstance(kwargs["power"], int):
                power = kwargs["power"]
            else:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return cast(F, wrapper)
    return decorator


def retry_spell(max_attempts: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}/"
                            f"{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return cast(F, wrapper)
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        time.sleep(0.01)
        return "Fireball cast!"

    print(fireball())

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("Boom!")

    print(unstable_spell())

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
