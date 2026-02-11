"""
This module implements complex validation rules for extraterrestrial
contact reports using Pydantic's model_validator.
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enumeration of allowed alien contact methods."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Represent an alien contact report with complex validation logic.

    Attributes:
        contact_id: ID starting with 'AC' (5-15 chars).
        timestamp: When the contact occurred.
        location: Where it happened (3-100 chars).
        contact_type: Method of contact.
        signal_strength: 0.0 to 10.0 scale.
        duration_minutes: Duration (1 to 1440 mins).
        witness_count: Number of witnesses (1 to 100).
        message_received: Optional message (max 500 chars).
        is_verified: Verification status.
    """

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        """Apply complex business rules for interstellar reports."""
        # ID Prefix check
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Physical contact must be verified
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Telepathic contact witness count
        is_telepathic = self.contact_type == ContactType.TELEPATHIC
        if is_telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        # Strong signals require a message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include messages")

        return self


def main() -> None:
    """Demonstrate valid and invalid contact report validation."""
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Valid Report
    try:
        report = AlienContact(
            contact_id="AC_2026_X1",
            timestamp="2026-02-11T20:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print("Valid contact report:")
        print(f"ID: {report.contact_id}")
        print(f"Type: {report.contact_type.value}")
        print(f"Signal: {report.signal_strength}/10")
        print(f"Message: '{report.message_received}'")
    except ValidationError as e:
        print(f"Unexpected Error: {e}")

    print("=" * 40)

    # Invalid Report (Telepathic with insufficient witnesses)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_BAD_01",
            timestamp=datetime.now(),
            location="Unknown",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=True
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
