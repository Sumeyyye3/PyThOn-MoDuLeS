#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return (temp_int)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")

    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print()
    print("Input data is 'abc'")

    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print()
    print("All tests completed - program didn't crash!")
