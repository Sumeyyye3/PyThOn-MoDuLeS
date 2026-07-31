from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field( min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) require at least "
                    "50% experienced crew (5+ years)"
                )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def print_values(mission: SpaceMission) -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
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
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )
        print("=========================================\n\n")


def testcases() -> None:
    try:
        valid_crew = [
            CrewMember(
                member_id="CM01",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=40,
                specialization="Mission Command",
                years_experience=12,
                is_active=True,
            ),
            CrewMember(
                member_id="CM02",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=6,
                is_active=True,
            ),
            CrewMember(
                member_id="CM03",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=3,
                is_active=True,
            ),
        ]

        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=valid_crew,
            budget_millions=2500.0,
        )
        print_values(valid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

    print("Expected validation error:")
    try:
        invalid_crew = [
            CrewMember(
                member_id="CM04",
                name="Bob Vance",
                rank=Rank.LIEUTENANT,
                age=30,
                specialization="Pilot",
                years_experience=4,
            ),
            CrewMember(
                member_id="CM05",
                name="Pam Beesly",
                rank=Rank.CADET,
                age=24,
                specialization="Communications",
                years_experience=1,
            )
        ]

        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Recon",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=invalid_crew,
            budget_millions=150.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


def main() -> None:
    testcases()


if __name__ == "__main__":
    main()
