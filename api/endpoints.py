"""
InboxOps API Endpoints
======================
REST API for the InboxOps platform.
"""
from flask import Blueprint, request, jsonify
from database import execute_query, search_users

api = Blueprint("api", __name__)

# VULN-57: API key for partner access hardcoded
PARTNER_API_KEY = "partner_key_FAKE_abc123def456"

@api.route("/api/v1/users/<user_id>")
def get_user_api(user_id):
    # VULN-58: No authentication required for user data endpoint
    # VULN-59: SQL injection via URL parameter
    results = execute_query(f"SELECT * FROM users WHERE id = '{user_id}'")
    return jsonify(results)

@api.route("/api/v1/users/search")
def search_api():
    q = request.args.get("q", "")
    # VULN-60: Unvalidated redirect via next parameter
    next_url = request.args.get("next", "/")
    results = search_users(q)
    return jsonify({"results": results, "redirect": next_url})

@api.route("/api/v1/export", methods=["POST"])
def export_data():
    format_type = request.json.get("format", "csv")
    query = request.json.get("query", "")
    # VULN-61: User-controlled SQL query executed directly
    results = execute_query(query)
    return jsonify(results)
