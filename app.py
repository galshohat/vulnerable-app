"""
InboxOps E-Commerce Platform - Main Application
================================================
A "production" Flask application with numerous security issues.
"""
import os
import pickle
import subprocess
import requests
from flask import Flask, request, jsonify, render_template_string, redirect
from database import get_user, execute_query
from auth import verify_token, create_token
from config import APP_CONFIG

# VULN-01: Debug mode enabled in production
app = Flask(__name__)
app.debug = True

# VULN-02: Secret key is hardcoded and weak
app.secret_key = "super-secret-key-123"

# VULN-03: CORS allows all origins with credentials
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# VULN-04: Slack webhook URL with token exposed in source
SLACK_WEBHOOK = "https://hooks.slack.com/services/T0FAKE01/B0FAKE02/xyzFakeWebhookToken1234567"

# VULN-05: Internal admin API key hardcoded
ADMIN_API_KEY = "ak_live_9a8b7c6d5e4f3g2h1i0j"


@app.route("/")
def index():
    name = request.args.get("name", "Guest")
    # VULN-06: Reflected XSS - user input rendered directly in HTML
    return render_template_string(f"""
        <html>
        <body>
            <h1>Welcome to InboxOps, {name}!</h1>
            <p>Your one-stop e-commerce support platform.</p>
        </body>
        </html>
    """)


@app.route("/search")
def search():
    query = request.args.get("q", "")
    # VULN-07: Stored XSS via search results rendered without escaping
    results = execute_query(f"SELECT * FROM products WHERE name LIKE '%{query}%'")
    html = "<h2>Search Results</h2><ul>"
    for r in results:
        html += f"<li>{r['name']} - ${r['price']}</li>"
    html += "</ul>"
    return render_template_string(html)


@app.route("/admin")
def admin_panel():
    # VULN-08: No authentication check on admin endpoint
    return jsonify({
        "users": execute_query("SELECT * FROM users"),
        "config": APP_CONFIG,
        "api_key": ADMIN_API_KEY,
    })


@app.route("/api/execute", methods=["POST"])
def execute_command():
    cmd = request.json.get("command", "")
    # VULN-09: OS command injection via user input
    result = os.popen(cmd).read()
    return jsonify({"output": result})


@app.route("/api/eval", methods=["POST"])
def eval_expression():
    expr = request.json.get("expression", "")
    # VULN-10: eval() with user-controlled input
    result = eval(expr)
    return jsonify({"result": str(result)})


@app.route("/api/run", methods=["POST"])
def run_script():
    script = request.json.get("script", "")
    # VULN-11: exec() with user-controlled input
    exec(script)
    return jsonify({"status": "executed"})


@app.route("/api/ping", methods=["POST"])
def ping_host():
    host = request.json.get("host", "")
    # VULN-12: Command injection via subprocess with shell=True
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return jsonify({"output": result.stdout})


@app.route("/api/fetch", methods=["POST"])
def fetch_url():
    url = request.json.get("url", "")
    # VULN-13: SSRF - fetches arbitrary URLs from user input
    response = requests.get(url)
    return jsonify({"status": response.status_code, "body": response.text[:1000]})


@app.route("/api/deserialize", methods=["POST"])
def deserialize_data():
    import base64
    data = request.json.get("data", "")
    # VULN-14: Insecure deserialization with pickle
    obj = pickle.loads(base64.b64decode(data))
    return jsonify({"result": str(obj)})


@app.route("/api/process", methods=["POST"])
def process_template():
    template = request.json.get("template", "")
    data = request.json.get("data", {})
    # VULN-15: Server-Side Template Injection (SSTI)
    rendered = render_template_string(template, **data)
    return rendered


@app.route("/error")
def trigger_error():
    try:
        1 / 0
    except Exception as e:
        # VULN-16: Verbose error messages expose internals
        import traceback
        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc(),
            "env": dict(os.environ),
        }), 500


@app.route("/health")
def health():
    # VULN-17: Health endpoint leaks system information
    return jsonify({
        "status": "ok",
        "python_version": os.popen("python --version").read(),
        "hostname": os.popen("hostname").read(),
        "whoami": os.popen("whoami").read(),
        "db_connection": str(APP_CONFIG["DATABASE_URL"]),
    })


if __name__ == "__main__":
    # VULN-18: Binding to all interfaces in production
    app.run(host="0.0.0.0", port=5000, debug=True)
