import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        exit()
    print("=== Cyber Archives Recovery ===")
    my_file = sys.argv[1]
    try:
        print(f"Accessing file '{my_file}'")
        text = open(my_file, "r")
        includes = text.read()
        print("---")
        print(includes)
        print("---")
        text.close()
        print(f"File '{my_file}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{my_file}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{my_file}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{my_file}': {e}")


if __name__ == "__main__":
    main()
