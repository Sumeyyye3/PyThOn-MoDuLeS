#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int >= 40:
        raise ValueError("100°C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError("-50°C is too cold for plants (min 0°C)")
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
    print("Input data is '100'")

    try:
        temp = input_temperature("100")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print()
    print("Input data is '-50'")

    try:
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
