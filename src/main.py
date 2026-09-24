"""
main.py — Combines SAST (code scanning), hardcoded secrets,
and command injection patterns into one file.
"""
import hashlib
import os
import pickle
import subprocess
import random

# ------------------------------------------------------------------
# HARDCODED SECRETS (Secret Scanning should flag these)
# ------------------------------------------------------------------
INTERNAL_API_KEY = "abcd1234efgh5678ijkl9012mnop3456"
JWT_SIGNING_KEY  = "super-secret-jwt-key-do-not-share"

# ------------------------------------------------------------------
# WEAK CRYPTO (Code Scanning)
# ------------------------------------------------------------------
def hash_password(password: str) -> str:
    """Uses MD5 — flagged by CodeQL as weak hashing."""
    return hashlib.md5(password.encode()).hexdigest()

def hash_legacy(value: str) -> str:
    """SHA1 is also weak."""
    return hashlib.sha1(value.encode()).hexdigest()

# ------------------------------------------------------------------
# DANGEROUS DESERIALIZATION (Code Scanning)
# ------------------------------------------------------------------
def load_session(blob: bytes):
    """pickle.loads on untrusted input -> arbitrary code execution."""
    return pickle.loads(blob)

# ------------------------------------------------------------------
# INSECURE RANDOMNESS (Code Scanning)
# ------------------------------------------------------------------
def generate_token() -> str:
    """random is not cryptographically secure."""
    return str(random.random())

# ------------------------------------------------------------------
# COMMAND INJECTION (Code Scanning + Injection testing)
# ------------------------------------------------------------------
def run_ping(host: str) -> str:
    """Shell injection: attacker controls `host`."""
    return subprocess.check_output(f"ping -c 1 {host}", shell=True).decode()

def run_backup(path: str) -> int:
    """Another shell injection vector."""
    return os.system("tar czf /tmp/backup.tar.gz " + path)

# ------------------------------------------------------------------
# UNSAFE EVAL (Code Scanning)
# ------------------------------------------------------------------
def calculate(expression: str):
    """eval on user input -> RCE."""
    return eval(expression)

def main():
    print(hash_password("admin"))
    print(generate_token())
    print(calculate("2 + 2"))

if __name__ == "__main__":
    main()
