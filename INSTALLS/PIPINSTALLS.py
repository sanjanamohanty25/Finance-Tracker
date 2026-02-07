import subprocess
import sys
import sysconfig
from pathlib import Path

BASE_DIR = Path(__file__).parent
REQUIREMENTS_FILE = BASE_DIR / "requirements.txt"


def get_stdlib_modules():
    """
    Returns a set of all Python standard library module names
    """
    stdlib_path = sysconfig.get_paths()["stdlib"]
    stdlib_modules = set()

    for path in Path(stdlib_path).iterdir():
        if path.is_dir():
            stdlib_modules.add(path.name)
        elif path.suffix == ".py":
            stdlib_modules.add(path.stem)

    # Common built-ins not present as files
    stdlib_modules.update({
        "sys", "os", "math", "time", "datetime", "calendar", "json",
        "re", "subprocess", "pathlib", "itertools", "functools"
    })

    return stdlib_modules


def clean_package(line: str) -> str:
    """
    Converts:
    'pip install tabulate' -> 'tabulate'
    """
    line = line.strip()
    if line.startswith("pip install"):
        return line.replace("pip install", "").strip()
    return line


def install_packages(file_path):
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    stdlib_modules = get_stdlib_modules()

    to_install = []
    skipped = []

    with open(file_path, "r") as file:
        for line in file:
            line
