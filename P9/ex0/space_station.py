#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 20)

    try:
        valide_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 8, 7, 22, 42, 42),
            is_operational=True,
        )
        print("Valid station created:")
        print(f"ID: {valide_station.station_id}")
        print(f"Name: {valide_station.name}")
        print(f"Crew: {valide_station.crew_size} people")
        print(f"Power: {valide_station.power_level}%")
        print(f"Oxygen: {valide_station.oxygen_level}%")
        status = (
            "Operational\n"
            if valide_station.is_operational
            else "Not Operational"
        )
        print(f"Status: {status}")
    except ValidationError as e:
        print(f"Erreur inattendue : {e}")

    print("=" * 20)
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id="ISS002",
            name="Test Station",
            crew_size=25,
            power_level=85.0,
            oxygen_level=92.0,
            last_maintenance=datetime(2026, 8, 7, 22, 42, 42),
            is_operational=True,
        )
        print("Valid station created:")
        print(f"ID: {valide_station.station_id}")
        print(f"Name: {valide_station.name}")
        print(f"Crew: {valide_station.crew_size} people")
        print(f"Power: {valide_station.power_level}%")
        print(f"Oxygen: {valide_station.oxygen_level}%")
        status = (
            "Operational\n"
            if valide_station.is_operational
            else "Not Operational"
        )
        print(f"Status: {status}")
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
