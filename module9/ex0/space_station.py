from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(..., max_length=200)


def print_values(obj_base: SpaceStation) -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {obj_base.station_id}")
    print(f"Name: {obj_base.name}")
    print(f"Crew: {obj_base.crew_size}")
    print(f"Power: {obj_base.power_level}")
    print(f"Oxygen: {obj_base.oxygen_level}")
    print(f"Status: {obj_base.is_operational}")
    print("========================================\n")


def main() -> None:
    try:
        obj_base = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Operational"
        )
        print_values(obj_base)
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'])

    try:
        obj_base = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=45,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Operational"
        )
        print_values(obj_base)
    except ValidationError as e:
        print("Expected validation error:")
        for msg in e.errors():
            print(msg['msg'])


if __name__ == "__main__":
    main()
