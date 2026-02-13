import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def print_directory_structure(path: Path, indent: int = 0):
    """Recursively print a directory tree with colored file and folder names."""
    for item in sorted(path.iterdir()):
        print(" " * indent, end="")

        if item.is_dir():
            print(Fore.BLUE + f"📂 {item.name}")
            print_directory_structure(item, indent + 4)
        else:
            print(Fore.GREEN + f"📜 {item.name}")


def main():
    """Validate CLI arguments and print the target directory structure."""
    if len(sys.argv) < 2:
        print("Provide directory path.")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print("Path does not exist.")
        return

    if not directory.is_dir():
        print("Provided path is not a directory.")
        return

    print_directory_structure(directory)


if __name__ == "__main__":
    main()
