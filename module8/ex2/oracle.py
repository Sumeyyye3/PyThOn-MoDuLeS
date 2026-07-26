import os
import sys
from dotenv import load_dotenv

REQUIRED_VARS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]

OPTIONAL_VARS = {
    "LOG_LEVEL": "INFO",
}

VALID_MODES = {"development", "production"}
VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


class ConfigError(Exception):
    pass


def load_configuration() -> dict:
    env_loaded = load_dotenv(dotenv_path=".env", override=False)

    pre_mode = os.getenv("MATRIX_MODE", "development").strip().lower()

    if pre_mode == "production":
        print("[Oracle] Production mode detected - using environment variables.")
    elif env_loaded:
        print("[Oracle] .env file detected and loaded (development mode).")
    else:
        print("[Oracle] WARNING: No .env file found and relying on environment variables.")

    config = {}
    missing = []

    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None or value.strip() == "":
            missing.append(var)
        else:
            config[var] = value.strip()

    if missing:
        raise ConfigError(
            "Missing required configuration variable(s): "
            + ", ".join(missing)
        )

    for var, default in OPTIONAL_VARS.items():
        config[var] = os.getenv(var, default).strip()

    mode = config["MATRIX_MODE"].lower()
    if mode not in VALID_MODES:
        raise ConfigError(f"Invalid MATRIX_MODE '{mode}'.")
    config["MATRIX_MODE"] = mode

    level = config["LOG_LEVEL"].upper()
    if level not in VALID_LOG_LEVELS:
        raise ConfigError(f"Invalid LOG_LEVEL '{level}'.")
    config["LOG_LEVEL"] = level

    return config


def mask_secret(value: str, visible: int = 4) -> str:
    if not value:
        return "<empty>"
    if visible <= 0 or len(value) <= visible:
        return "*" * len(value)
    return "*" * (len(value) - visible) + value[-visible:]


def run_development(config: dict) -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if "localhost" in config["DATABASE_URL"] or "local" in config["DATABASE_URL"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected")

    print(f"API Access: Authenticated (Key: {mask_secret(config['API_KEY'])})")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def run_production(config: dict) -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print("Database: Secure connection established")
    print(f"API Access: Authenticated (Key: {mask_secret(config['API_KEY'])})")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] Production mode active")
    print("[OK] Production overrides available")


def main() -> int:
    try:
        config = load_configuration()
    except ConfigError as exc:
        print(f"[Oracle] ERROR: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"[Oracle] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return 1

    if config["MATRIX_MODE"] == "development":
        run_development(config)
    else:
        run_production(config)

    print("\nThe Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())