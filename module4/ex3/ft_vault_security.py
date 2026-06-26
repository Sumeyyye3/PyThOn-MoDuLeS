def secure_archive(
    filename: str,
    mode: str = "r",
    content: str | None = None,
) -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(filename, "r") as file:
                return (True, file.read())

        elif mode == "w":
            if content is None:
                return (False, "Content is required for write mode")

            with open(filename, "w") as file:
                file.write(content)

            return (True, "Content successfully written to file")

        return (False, "Invalid mode")

    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test.txt", "w", "Content here"))


if __name__ == "__main__":
    main()
