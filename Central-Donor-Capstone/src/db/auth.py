"""Local login accounts for Donor Manager.

Passwords are never stored. Only a random salt and a PBKDF2 hash are kept
in a small SQLite file in the user's AppData folder.
"""
import hashlib
import hmac
import os
import sqlite3
from pathlib import Path

ITERATIONS = 200_000
MIN_PASSWORD_LENGTH = 8


def _db_path() -> Path:
    base = Path(os.getenv("APPDATA", Path.home())) / "DonorManager"
    base.mkdir(parents=True, exist_ok=True)
    return base / "users.db"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(_db_path())
    conn.execute(
        """CREATE TABLE IF NOT EXISTS users (
               username TEXT PRIMARY KEY COLLATE NOCASE,
               salt     BLOB NOT NULL,
               hash     BLOB NOT NULL,
               is_admin INTEGER NOT NULL DEFAULT 0
           )"""
    )
    return conn


def _hash(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)


def has_users() -> bool:
    with _connect() as conn:
        return conn.execute("SELECT 1 FROM users LIMIT 1").fetchone() is not None


def create_user(username: str, password: str, is_admin: bool = False) -> None:
    salt = os.urandom(16)
    with _connect() as conn:
        conn.execute(
            "INSERT INTO users (username, salt, hash, is_admin) VALUES (?, ?, ?, ?)",
            (username.strip(), salt, _hash(password, salt), int(is_admin)),
        )


def verify_login(username: str, password: str) -> bool:
    with _connect() as conn:
        row = conn.execute(
            "SELECT salt, hash FROM users WHERE username = ?", (username.strip(),)
        ).fetchone()
    if row is None:
        # Hash anyway so a wrong username takes as long as a wrong password.
        _hash(password, b"\x00" * 16)
        return False
    salt, stored = row
    return hmac.compare_digest(_hash(password, salt), stored)