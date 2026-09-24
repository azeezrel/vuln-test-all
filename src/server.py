"""
server.py — Web-layer injection surface (command injection, SSTI,
SSRF, path traversal, XSS).
"""
import os
import requests
from flask import Flask, request, render_template_string, Response

app = Flask(__name__)

# ------------------------------------------------------------------
# COMMAND INJECTION
# ------------------------------------------------------------------
@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    output = os.popen(f"ping -c 1 {host}").read()   # ❌ command injection
    return Response(output, mimetype="text/plain")

@app.route("/dns")
def dns():
    name = request.args.get("name", "")
    return os.popen("nslookup " + name).read()      # ❌ command injection

# ------------------------------------------------------------------
# PATH TRAVERSAL
# ------------------------------------------------------------------
@app.route("/read")
def read_file():
    filename = request.args.get("file", "")
    path = os.path.join("/var/data", filename)
    with open(path, "r") as f:                      # ❌ path traversal
        return f.read()

# ------------------------------------------------------------------
# SERVER-SIDE TEMPLATE INJECTION (SSTI)
# ------------------------------------------------------------------
@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    template = "Hello " + name + "!"                # ❌ SSTI
    return render_template_string(template)

# ------------------------------------------------------------------
# SSRF
# ------------------------------------------------------------------
@app.route("/fetch")
def fetch():
    url = request.args.get("url", "http://example.com")
    r = requests.get(url, timeout=5)                # ❌ SSRF
    return Response(r.text, mimetype="text/plain")

# ------------------------------------------------------------------
# REFLECTED XSS
# ------------------------------------------------------------------
@app.route("/search")
def search():
    q = request.args.get("q", "")
    html = f"<html><body><h1>Results for {q}</h1></body></html>"
    return Response(html, mimetype="text/html")     # ❌ XSS

if __name__ == "__main__":
    app.run(debug=True)
