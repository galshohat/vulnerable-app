"""
InboxOps Application Configuration
===================================
Central configuration for the InboxOps platform.
"""
import os

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Payment processing
STRIPE_SECRET_KEY = "rk_live_FAKE_51HG3bDK8x2m4KeyHere1234567890abcdef"
STRIPE_PUBLISHABLE_KEY = "pk_live_51HG3bDK8x2m4FAKE0RealKeyHere1234567890abcdef"

SENDGRID_API_KEY = "SG.fakekey123456789.ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk"

# OAuth credentials
GITHUB_CLIENT_SECRET = "ghs_FakeGitHubClientSecret1234567890ABCDEF"

SMTP_CONFIG = {
    "host": "smtp.inboxops.com",
    "port": 587,
    "username": "noreply@inboxops.com",
    "password": "SmTp_Pr0d_2024!SecureNot",
}

APP_CONFIG = {
    "DEBUG": True,
    "DATABASE_URL": "postgresql://inboxops_admin:Pr0d_DB_P@ssw0rd!2024@prod-db.inboxops.internal:5432/inboxops_production",
    "SECRET_KEY": "super-secret-key-123",
    "SESSION_COOKIE_SECURE": False,
    "SESSION_COOKIE_HTTPONLY": False,
    "CORS_ORIGINS": "*",
    "CORS_SUPPORTS_CREDENTIALS": True,
    "RATE_LIMIT_ENABLED": False,
}

ENCRYPTION_KEY = b"0123456789abcdef"
ENCRYPTION_IV = b"0000000000000000"
