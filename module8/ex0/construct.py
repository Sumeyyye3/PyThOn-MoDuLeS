import sys
import site
import os


def real_env() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print("Current Python:", sys.prefix)
    print()
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print()
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print()
    print("python -m venv matrix_env")
    print()
    print("source matrix_env/bin/activate # On Unix")
    print()
    print("matrix_env"+"\\"+"Scripts"+"\\"+"activate # On Windows")
    print()
    print("Then run this program again.")


def construct_env() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print("Current Python:", sys.executable)
    print()
    print("Virtual Environment:", os.path.basename(p=sys.prefix))
    print()
    print("Environment Path:", os.path.dirname(
        os.path.dirname(p=sys.executable)))
    print()
    print("SUCCESS: You're in an isolated environment!")
    print()
    print("Safe to install packages without affecting")
    print()
    print("the global system.")
    print()
    print("Package installation path:")
    print()
    print(site.getsitepackages()[0])


def main() -> None:
    if sys.prefix == sys.base_prefix:
        real_env()
    else:
        construct_env()


if __name__ == "__main__":
    main()
