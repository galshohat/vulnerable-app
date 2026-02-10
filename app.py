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

app = Flask(__name__)
app.debug = True

app.secret_key = "super-secret-key-123"

from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

SLACK_WEBHOOK = "https://hooks.slack.com/services/T0FAKE01/B0FAKE02/xyzFakeWebhookToken1234567"

ADMIN_API_KEY = "ak_live_9a8b7c6d5e4f3g2h1i0j"


@app.route("/")
def index():
    name = request.args.get("name", "Guest")
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
    results = execute_query(f"SELECT * FROM products WHERE name LIKE '%{query}%'")
    html = "<h2>Search Results</h2><ul>"
    for r in results:
        html += f"<li>{r['name']} - ${r['price']}</li>"
    html += "</ul>"
    return render_template_string(html)


@app.route("/admin")
def admin_panel():
    return jsonify({
        "users": execute_query("SELECT * FROM users"),
        "config": APP_CONFIG,
        "api_key": ADMIN_API_KEY,
    })


@app.route("/api/execute", methods=["POST"])
def execute_command():
    cmd = request.json.get("command", "")
    result = os.popen(cmd).read()
    return jsonify({"output": result})


@app.route("/api/eval", methods=["POST"])
def eval_expression():
    expr = request.json.get("expression", "")
    result = eval(expr)
    return jsonify({"result": str(result)})


@app.route("/api/run", methods=["POST"])
def run_script():
    script = request.json.get("script", "")
    exec(script)
    return jsonify({"status": "executed"})


@app.route("/api/ping", methods=["POST"])
def ping_host():
    host = request.json.get("host", "")
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return jsonify({"output": result.stdout})


@app.route("/api/fetch", methods=["POST"])
def fetch_url():
    url = request.json.get("url", "")
    response = requests.get(url)
    return jsonify({"status": response.status_code, "body": response.text[:1000]})


@app.route("/api/deserialize", methods=["POST"])
def deserialize_data():
    import base64
    data = request.json.get("data", "")
    obj = pickle.loads(base64.b64decode(data))
    return jsonify({"result": str(obj)})


@app.route("/api/process", methods=["POST"])
def process_template():
    template = request.json.get("template", "")
    data = request.json.get("data", {})
    rendered = render_template_string(template, **data)
    return rendered


@app.route("/error")
def trigger_error():
    try:
        1 / 0
    except Exception as e:
        import traceback
        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc(),
            "env": dict(os.environ),
        }), 500


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "python_version": os.popen("python --version").read(),
        "hostname": os.popen("hostname").read(),
        "whoami": os.popen("whoami").read(),
        "db_connection": str(APP_CONFIG["DATABASE_URL"]),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
