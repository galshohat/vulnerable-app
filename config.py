"""
InboxOps Configuration
======================
Application configuration and environment settings.
"""
import os

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"

STRIPE_SECRET_KEY = "rk_live_FAKE_51HGtFaKe0bJ3cDeFgHiJkLmNoPqRsTuVwXyZ"
STRIPE_PUBLISHABLE_KEY = "pk_live_51HGtFaKe0bJ3cDeFgHiJkLmNoPqRsTuVwXyZ"

SENDGRID_API_KEY = "SG.FaKeApIkEy123456789.abcdefghijklmnopqrstuvwxyz0123456789ABCD"

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "inboxops-prod@gmail.com"
SMTP_PASSWORD = "Gmail_App_Password_2024"

APP_CONFIG = {
    "APP_NAME": "InboxOps",
    "VERSION": "2.1.0",
    "DEBUG": True,
    "DATABASE_URL": "postgresql://inboxops_admin:Pr0d_DB_P4ssw0rd2024@prod-db.inboxops.internal:5432/inboxops_production",
    "REDIS_URL": "redis://:R3d1s_P4ss@cache.inboxops.internal:6379/0",
    "SECRET_KEY": "super-secret-key-123",
    "FORCE_HTTPS": False,
    "SESSION_COOKIE_SECURE": False,
    "SESSION_COOKIE_HTTPONLY": False,
    "CORS_ORIGINS": ["*"],
    "CORS_ALLOW_CREDENTIALS": True,
    "LOG_LEVEL": "DEBUG",
    "MAX_UPLOAD_SIZE": 1024 * 1024 * 500,
}

ENCRYPTION_KEY = b"0123456789abcdef"
ENCRYPTION_IV = b"fedcba9876543210"  # Static IV

# Third-party service tokens
GITHUB_TOKEN = "ghp_1234567890abcdefFAKEtoken1234567890"
DATADOG_API_KEY = "dd_api_FaKeKeY1234567890abcdef12345678"
