import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        exit()

    print("=== Cyber Archives Recovery & Preservation ===")
    my_file = sys.argv[1]

    try:
        print(f"Accessing file '{my_file}'")

        text = open(my_file, "r")
        includes = text.read()
        text.close()

        print("---\n")
        print(includes)
        print("---")
        print(f"File '{my_file}' closed.")

        print("\nTransform data:")
        print("---\n")

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

        print("Enter new file name (or empty): ", end="", flush=True)
        new_file = sys.stdin.readline().strip()

        if new_file == "":
            print("Data not saved.")
        else:
            try:
                print(f"Saving data to '{new_file}'")
                obj_file = open(new_file, "w")
                obj_file.write(new_includes)
                obj_file.close()
                print(f"Data saved in file '{new_file}'.")
            except Exception as e:
                sys.stderr.write(
                    f"[STDERR] Error opening file '{new_file}': {e}\n"
                )
                print("Data not saved.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{my_file}': {e}\n")


if __name__ == "__main__":
    main()
