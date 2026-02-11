"""
This module defines the SpaceStation model using Pydantic to ensure
data integrity for cosmic research facilities.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
    Represent a space station with validated orbital statistics.

    Attributes:
        station_id: Unique identifier (3-10 characters).
        name: Name of the station (1-50 characters).
        crew_size: Number of personnel (1-20).
        power_level: Energy percentage (0-100).
        oxygen_level: Oxygen percentage (0-100).
        last_maintenance: Timestamp of the last check-up.
        is_operational: Operational status of the station.
        notes: Optional additional information (max 200 characters).
    """

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    """Run demonstration of valid and invalid SpaceStation models."""
    print("Space Station Data Validation")
    print("=" * 40)

    # Creating a valid station instance
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-02-10T12:00:00",
            notes="All systems functional."
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        status = "Operational" if valid_station.is_operational else "Offline"
        print(f"Status: {status}")

    except ValidationError as e:
        print(f"Unexpected Validation Error: {e.json()}")

    print("=" * 40)

    # Attempting to create an invalid station (crew_size > 20)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="EX-01",
            name="Alpha Centauri Outpost",
            crew_size=25,  # Invalid: exceeds maximum of 20
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        # Extracting the human-readable message from the first error
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
