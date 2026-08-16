from collections.abc import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int
                    ) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_powerful(target: str, power: int) -> bool:
        return power > 50

    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 40))

    amplified = power_amplifier(fireball, 3)
    print(amplified("Dragon", 10))

    cond = conditional_caster(is_powerful, fireball)
    print(cond("Dragon", 60))
    print(cond("Dragon", 30))

    seq = spell_sequence([fireball, heal])
    print(seq("Dragon", 50))
