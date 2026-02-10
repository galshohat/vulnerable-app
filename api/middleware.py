"""
InboxOps API Middleware
=======================
Request/response middleware for the API.
"""
import logging
import traceback

logger = logging.getLogger(__name__)

def error_handler(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        # VULN-62: Full stack trace returned to client
        return {
            "error": str(e),
            "type": type(e).__name__,
            "traceback": traceback.format_exc(),
        }, 500

def request_logger(app):
    @app.before_request
    def log_request():
        from flask import request
        # VULN-63: Logging request bodies including passwords and tokens
        logger.info(f"Request: {request.method} {request.path} Body: {request.get_data(as_text=True)}")
