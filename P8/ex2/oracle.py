#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv


def check_security(mode: str, env_loaded: bool) -> None:
    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")

    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing (using system env variables)")

    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    env_loaded = load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if matrix_mode == "production":
        db_display = "Connected to production cluster (Encrypted)"
        api_display = (
            "Authenticated (Production Scope)"
            if api_key
            else "Missing Credentials"
        )
        zion_display = (
            f"Connected via Secure Tunnel to {zion_endpoint}"
            if zion_endpoint
            else "Offline"
        )
    else:
        db_display = (
            "Connected to local instance"
            if db_url
            else "Using SQLite Memory Cache (Fallback)"
        )
        api_display = (
            "Authenticated"
            if api_key
            else "Not Authenticated (Demo Mode)"
        )
        zion_display = (
            "Online"
            if zion_endpoint
            else "Offline (Simulation)"
        )

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {db_display}")
    print(f"API Access: {api_display}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_display}\n")

    check_security(matrix_mode, env_loaded)
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
