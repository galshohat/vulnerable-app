"""
InboxOps Configuration
======================
Application configuration and environment settings.
"""
import os

# VULN-38: AWS credentials hardcoded in source
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"

# VULN-39: Stripe API keys in source
STRIPE_SECRET_KEY = "rk_live_FAKE_51HGtFaKe0bJ3cDeFgHiJkLmNoPqRsTuVwXyZ"
STRIPE_PUBLISHABLE_KEY = "pk_live_51HGtFaKe0bJ3cDeFgHiJkLmNoPqRsTuVwXyZ"

# VULN-40: SendGrid API key hardcoded
SENDGRID_API_KEY = "SG.FaKeApIkEy123456789.abcdefghijklmnopqrstuvwxyz0123456789ABCD"

# VULN-41: SMTP credentials in plaintext
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "inboxops-prod@gmail.com"
SMTP_PASSWORD = "Gmail_App_Password_2024"

APP_CONFIG = {
    "APP_NAME": "InboxOps",
    "VERSION": "2.1.0",
    # VULN-42: Debug enabled in production config
    "DEBUG": True,
    # VULN-43: Database URL with credentials in config dict
    "DATABASE_URL": "postgresql://inboxops_admin:Pr0d_DB_P4ssw0rd2024@prod-db.inboxops.internal:5432/inboxops_production",
    "REDIS_URL": "redis://:R3d1s_P4ss@cache.inboxops.internal:6379/0",
    "SECRET_KEY": "super-secret-key-123",
    # VULN-44: No HTTPS enforcement
    "FORCE_HTTPS": False,
    "SESSION_COOKIE_SECURE": False,
    "SESSION_COOKIE_HTTPONLY": False,
    # VULN-45: Overly permissive CORS
    "CORS_ORIGINS": ["*"],
    "CORS_ALLOW_CREDENTIALS": True,
    "LOG_LEVEL": "DEBUG",
    "MAX_UPLOAD_SIZE": 1024 * 1024 * 500,
}

# VULN-46: Encryption key hardcoded
ENCRYPTION_KEY = b"0123456789abcdef"
ENCRYPTION_IV = b"fedcba9876543210"  # Static IV

# Third-party service tokens
GITHUB_TOKEN = "ghp_1234567890abcdefFAKEtoken1234567890"
DATADOG_API_KEY = "dd_api_FaKeKeY1234567890abcdef12345678"
