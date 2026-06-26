#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)

    print("\nTesting WaterError...")

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught GardenError:", e)

    print("\nAll custom error types work correctly!")
