"""

This module manages complex nested data structures for space missions,
ensuring safety protocols through multi-model validation.
"""

from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Crew ranks authorized for interstellar missions."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Individual crew member data model.

    Attributes:
        member_id: ID (3-10 chars).
        name: Full name (2-50 chars).
        rank: Official rank.
        age: Age between 18 and 80.
        specialization: Area of expertise.
        years_experience: Years in service (0-50).
        is_active: Current duty status.
    """

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Space mission model containing a nested list of crew members.

    Attributes:
        mission_id: ID starting with 'M' (5-15 chars).
        mission_name: Name (3-100 chars).
        destination: Target (3-50 chars).
        launch_date: Planned date.
        duration_days: Duration (1-3650 days).
        crew: List of 1-12 CrewMember objects.
        mission_status: Current phase.
        budget_millions: Cost in millions (1.0-10000.0).
    """

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        """Enforce interstellar safety and command protocols."""
        # Mission ID prefix
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Hierarchy check (Captain or Commander required)
        leadership_ranks = {Rank.CAPTAIN, Rank.COMMANDER}
        has_leader = any(m.rank in leadership_ranks for m in self.crew)
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        # Long mission experience check
        if self.duration_days > 365:
            exp_crew = [m for m in self.crew if m.years_experience >= 5]
            if len(exp_crew) < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew"
                )

        # Active status check
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Run demonstration for SpaceMission validation."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    # Valid Mission
    try:
        crew = [
            CrewMember(
                member_id="ID_01", name="Sarah Connor", rank=Rank.COMMANDER,
                age=45, specialization="Mission Command", years_experience=20
            ),
            CrewMember(
                member_id="ID_02", name="John Smith", rank=Rank.LIEUTENANT,
                age=30, specialization="Navigation", years_experience=6
            ),
            CrewMember(
                member_id="ID_03", name="Alice Johnson", rank=Rank.OFFICER,
                age=25, specialization="Engineering", years_experience=2
            )
        ]
        mission = SpaceMission(
            mission_id="M2026_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-06-01T08:00:00",
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
        )
        print(f"Valid mission created:\nMission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}\nDestination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M\nCrew size: {len(crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected Validation Error: {e}")

    print("=" * 41)

    # Invalid Mission (Missing Leader)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M_FAIL_01",
            mission_name="Failed Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="ID_X", name="Newbie", rank=Rank.CADET,
                    age=19, specialization="Cleaning", years_experience=0
                )
            ],
            budget_millions=100.0
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
