import sys
import os
import site


def main() -> None:
    in_matrix: bool = sys.prefix != sys.base_prefix

    if in_matrix:
        print("MATRIX STATUS: Welcome to the construct\n")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    if in_matrix:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system")
        print("\nPackage installation path:")
        for path in site.getsitepackages():
            print(path)
    else:
        print("Virtual Environment: None detected\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again")


if __name__ == "__main__":
    main()
