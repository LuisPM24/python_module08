import importlib
import sys


def load_dependency(item: str) -> object | None:
    try:
        return importlib.import_module(item)
    except ImportError:
        return None


def manage_dependencies(dependencies: dict[str, str]) -> bool:
    return_value = True
    for item, message in dependencies.items():
        dependency = load_dependency(item)
        if dependency is None:
            print(f"[KO] {item} - Not Installed")
            return_value = False
        else:
            print(
                f"[OK] {item} {getattr(dependency, '__version__', 'unknown')}"
                f" - {message}"
                )
    return return_value


def main() -> None:
    dependencies = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
    }

    print("LOADING STATUS: Loading programs...\n")
    if manage_dependencies(dependencies) is False:
        print(
            "\nInstall dependencies with pip:\n"
            "pip install -r requirements.txt\n\n"
            "Or with Poetry:\n"
            "poetry install\n"
            "poetry run python loading.py\n"
        )
        sys.exit(1)
    else:
        print(
            "\nAnalyzing Matrix data...\n"
            "Processing 1000 data points...\n"
            "Generating visualization...\n\n"
            "Analysis complete!"
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
