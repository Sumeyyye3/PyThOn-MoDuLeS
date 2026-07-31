from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_alien_contact_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def print_values(obj_base: AlienContact) -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {obj_base.contact_id}")
    print(f"Type: {obj_base.contact_type.value}")
    print(
        f"Location: {obj_base.location}"
    )
    print(f"Signal: {obj_base.signal_strength}/10")
    print(
        f"Duration: "
        f"{obj_base.duration_minutes} minutes"
    )
    print(f"Witnesses: {obj_base.witness_count}")
    print(f"Message: '{obj_base.message_received}'")
    print("\n======================================")


def testcases() -> None:
    try:
        obj_base1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        print_values(obj_base1)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

    print("Expected validation error:")

    try:
        obj_base2 = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Siberia, Russia",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=2,
            is_verified=False,
        )
        print_values(obj_base2)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


def main() -> None:
    testcases()


if __name__ == "__main__":
    main()
