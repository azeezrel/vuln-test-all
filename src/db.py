"""
db.py — SQL Injection patterns for injection-scanning tests.
"""
import sqlite3

def _conn():
    return sqlite3.connect("app.db")

# ------------------------------------------------------------------
# CLASSIC CONCATENATION SQLi
# ------------------------------------------------------------------
def get_user_by_name(username: str):
    conn = _conn()
    cur = conn.cursor()
    query = "SELECT id, name, email FROM users WHERE name = '" + username + "'"
    cur.execute(query)                 # ❌ SQLi
    return cur.fetchall()

# ------------------------------------------------------------------
# F-STRING SQLi
# ------------------------------------------------------------------
def get_user_by_id(user_id: str):
    conn = _conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")   # ❌ SQLi
    return cur.fetchall()

# ------------------------------------------------------------------
# DELETE with raw interpolation
# ------------------------------------------------------------------
def delete_user(user_id: str):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s" % user_id)   # ❌ SQLi
    conn.commit()

# ------------------------------------------------------------------
# ORDER BY injection (often missed by naive scanners)
# ------------------------------------------------------------------
def list_users(sort_column: str):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY " + sort_column) # ❌ SQLi
    return cur.fetchall()

# ------------------------------------------------------------------
# SAFE EXAMPLE (contrast — should NOT be flagged)
# ------------------------------------------------------------------
def safe_get_user(username: str):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (username,))
    return cur.fetchall()
