from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda item: item['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda item: f"* {item} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_pw = max(mages, key=lambda item: item['power'])['power']
    min_pw = min(mages, key=lambda item: item['power'])['power']
    avg_pw = round(sum(map(lambda item: item['power'], mages)) / len(mages), 2)
    return {"max_power": max_pw, "min_power": min_pw, "avg_power": avg_pw}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Storm Crown', 'power': 111, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 71, 'type': 'relic'}
    ]
    mages = [
        {'name': 'Casey', 'power': 98, 'element': 'water'},
        {'name': 'Riley', 'power': 59, 'element': 'fire'}
    ]
    spells = ['fireball', 'heal']

    print(artifact_sorter(artifacts))
    print(power_filter(mages, 90))
    print(spell_transformer(spells))
    print(mage_stats(mages))
