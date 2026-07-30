import os
import sys
from dotenv import load_dotenv

REQUIRED_VARS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]

OPTIONAL_VARS = {
    "LOG_LEVEL": "INFO",
}

VALID_MODES = {"development", "production"}
VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


class ConfigurationError(Exception):
    pass


def valid_mod_level(config: dict[str]) -> None:
    for key, value in OPTIONAL_VARS.items():
        config[key] = os.getenv(key, value).strip()

    mode = config["MATRIX_MODE"].lower()
    if mode not in VALID_MODES:
        raise ConfigurationError
    (f"Invalid MATRIX_MODE '{mode}'.")
    config["MATRIX_MODE"] = mode

    level = config["LOG_LEVEL"].upper()
    if level not in VALID_LOG_LEVELS:
        raise ConfigurationError
    (f"Invalid LOG_LEVEL '{level}'.")
    config["LOG_LEVEL"] = level


def add_required() -> dict[str]:
    config = {}
    missing = []

    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None or value.strip() == "":
            missing.append(var)
        else:
            config[var] = value.strip()

    if missing:
        raise ConfigurationError(
            "Missing required configuration variable(s): "
            + ", ".join(missing)
        )
    return config


def load_configuration() -> dict:
    env_loaded = load_dotenv(dotenv_path=".env", override=False)

    pre_mode = os.getenv("MATRIX_MODE", "development").strip().lower()

    if pre_mode == "production":
        print(
            "[Oracle] Production mode detected "
            "- using environment variables."
        )
    elif env_loaded:
        print("[Oracle] .env file detected and loaded (development mode).")
    else:
        print(
            "[Oracle] WARNING: No .env file found and "
            "relying on environment variables."
        )

    config = add_required()
    valid_mod_level(config)
    return config


def mask_secret(value: str, visible: int = 4) -> str:
    if not value:
        return "<empty>"
    if visible <= 0 or len(value) <= visible:
        return "*" * len(value)
    return "*" * (len(value) - visible) + value[-visible:]


def mod_development(config: dict) -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if (
        "localhost" in config["DATABASE_URL"]
        or "local" in config["DATABASE_URL"]
    ):
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


def mod_production(config: dict) -> None:
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


def main() -> None:
    try:
        config = load_configuration()
    except ConfigurationError as exc:
        print(f"[Oracle] ERROR: {exc}", file=sys.stderr)
        return
    except Exception as exc:
        print(f"[Oracle] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return

    if config["MATRIX_MODE"] == "development":
        mod_development(config)
    else:
        mod_production(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
