import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        exit()
    print("=== Cyber Archives Recovery & Preservation ===")
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

        print("\nTransform data:")
        print("---")
        new_includes = ""
        current_line = ""
        for char in includes:
            if char == "\n":
                new_includes += current_line + "#\n"
                current_line = ""
            else:
                current_line += char
        if current_line:
            new_includes += current_line + "#\n"

        print(new_includes)

        print("---")
        new_file = input("Enter new file name (or empty): ")
        if new_file == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            obj_file = open(new_file, "w")
            obj_file.write(new_includes)
            obj_file.close()
            print(f"Data saved in file '{new_file}'.\n")
    except FileNotFoundError as e:
        print(f"Error opening file '{my_file}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{my_file}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{my_file}': {e}")


if __name__ == "__main__":
    main()
