# vuln-test-all

Combined vulnerability test repository for security-tool validation.

## Contains
- **Code Scanning (SAST)** → `src/main.py`, `src/server.py`, `src/db.py`
- **Secret Scanning** → `src/auth.py`, `config/secrets.env`
- **Code Injection** → `src/db.py` (SQLi), `src/server.py` (CMDi, SSTI, SSRF, XSS, path traversal)
- **Dependency Scanning** → `requirements.txt`, `package.json`

## Enable on GitHub
1. Settings → Code security and analysis
2. Turn on: Dependabot alerts, Dependabot security updates, Code scanning (CodeQL), Secret scanning, Push protection.

## ⚠️ Warning
All credentials here are **fake** and meant for testing only.
Push only to a throwaway account.
