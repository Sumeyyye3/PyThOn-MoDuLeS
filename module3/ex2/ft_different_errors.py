#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        int(42) / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "42" + 42
    elif operation_number == 4:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while (i < 4):
        print(f"Testing operation {i}...")

        try:
            garden_operations(i)
        except ValueError as e:
            print("Caught ValueError:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except TypeError as e:
            print("Caught TypeError:", e)
        i = i + 1
    print("Testing operation 4...")
    garden_operations(4)
    print("\nAll error types tested successfully!")
