#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import List, Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class RankEnum(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")

        required_ranks = [RankEnum.COMMANDER, RankEnum.CAPTAIN]
        has_high_rank = any(m.rank in required_ranks for m in self.crew)
        if not has_high_rank:
            raise ValueError(
                "Mission must have at least one \
Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% \
experienced crew (5+ years)"
                )

        inactive_members = [m.name for m in self.crew if not m.is_active]
        if inactive_members:
            raise ValueError(
                f"All crew members must be active. \
Inactive: {', '.join(inactive_members)}"
            )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 20)

    try:
        crew_valid = [
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=RankEnum.COMMANDER,
                age=40,
                specialization="Mission Command",
                years_experience=15,
                is_active=True,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=RankEnum.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=6,
                is_active=True,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=RankEnum.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=4,
                is_active=True,
            ),
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=crew_valid,
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} \
({member.rank.value}) - {member.specialization}"
            )

    except ValidationError as e:
        print(f"Excepted error : {e}")
    print("")
    print("=" * 20)

    try:
        crew_invalid = [
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=RankEnum.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=6,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=RankEnum.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=5,
            ),
        ]

        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=crew_invalid,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
