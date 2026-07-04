import os
import sys


def security_check(data: dict[str, str | None]) -> None:
    script_dir = os.path.dirname(__file__)
    env_path = os.path.join(script_dir, ".env")

    print("\nEnvironment security check:")

    if os.path.isfile(env_path) is False:
        print("[KO] Hardcoded secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if data["MATRIX_MODE"] == "production":
        print("[OK] Production mode active")
        print("[OK] Production overrides available")
    else:
        print("[OK] Development mode active")
        print("[KO] Production overrides unavailable")


def load_config(required_env: list[str]) -> dict[str, str | None]:
    data: dict[str, str | None] = {}

    try:
        from dotenv import load_dotenv
        load_dotenv(override=False)
    except ImportError as e:
        print(f"ERROR - The program cannot read the .env variables: {e}")
        sys.exit(1)
    for key in required_env:
        data[key] = os.getenv(key)
    return data


def show_config(data: dict[str, str | None]) -> None:
    if data["MATRIX_MODE"] == "production":
        print("Mode: Production")
        print("Runtime: Secure production configuration")
        print("Debug tools: Disabled")
    else:
        print("Mode: Development")
        print("Runtime: Local development configuration")
        print("Debug tools: Enabled")

    if not data["DATABASE_URL"]:
        print("\nWARNING - Missing database. Using local instance instead\n")
        print("Database: Connected to local instance")
    else:
        print(f"Database: Connected to {data['DATABASE_URL']}")

    if not data["API_KEY"]:
        print("API Access: Unauthorized")
    else:
        print("API Access: Authorized")

    print(f"Log level: {data['LOG_LEVEL']}")

    if not data["ZION_ENDPOINT"]:
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")


def main() -> None:
    required_env = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                    "ZION_ENDPOINT"]

    print("ORACLE STATUS: Reading the Matrix...\n")
    data = load_config(required_env)
    print("Configuration file loaded.\n")
    show_config(data)
    security_check(data)


if __name__ == "__main__":
    main()
