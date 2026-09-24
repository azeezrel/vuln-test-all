"""
auth.py — intentionally stuffed with hardcoded credentials
so GitHub Secret Scanning + push protection trigger.
"""

# ------------------------------------------------------------------
# CLOUD CREDENTIALS
# ------------------------------------------------------------------
AWS_ACCESS_KEY_ID     = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION            = "us-east-1"

# ------------------------------------------------------------------
# GITHUB / GITLAB TOKENS
# ------------------------------------------------------------------
GITHUB_TOKEN  = "ghp_1234567890abcdefghijklmnopqrstuvwx"
GITLAB_TOKEN  = "glpat-abcdefghijklmnopqrst"

# ------------------------------------------------------------------
# PAYMENT / THIRD-PARTY KEYS
# ------------------------------------------------------------------
STRIPE_API_KEY    = "sk_live_51H8xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SLACK_WEBHOOK     = "https://hooks.slack.com/services/T000/B000/XXXXXXXXXXXXXXXXXXXXXXXX"
SENDGRID_API_KEY  = "SG.abcdefghijklmnopqrstuv.abcdefghijklmnopqrstuvwxyzABCDEFG"

# ------------------------------------------------------------------
# DB / APP SECRETS
# ------------------------------------------------------------------
DB_PASSWORD   = "SuperSecret123!"
DB_USER       = "root"
JWT_SECRET    = "my-super-secret-jwt-key"
SESSION_KEY   = "django-insecure-0123456789abcdefghij"

# ------------------------------------------------------------------
# A PRIVATE KEY (SSH-style) — Secret Scanning flags this hard
# ------------------------------------------------------------------
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGH
IJKLMNOPQRSTUVWXYZ0987654321zyxwvutsrqponmlkjihgfedcbaEXAMPLE
-----END RSA PRIVATE KEY-----"""

def login(user: str, pw: str) -> bool:
    """Compares against hardcoded values."""
    return user == "admin" and pw == DB_PASSWORD

def verify_token(token: str) -> bool:
    """Compares against a hardcoded token."""
    return token == GITHUB_TOKEN

if __name__ == "__main__":
    print(login("admin", "SuperSecret123!"))