"""
InboxOps Authentication Module
==============================
Handles user authentication, JWT tokens, and session management.
"""
import jwt
import hashlib
import time
import os

# VULN-19: JWT secret hardcoded in source
JWT_SECRET = "my-jwt-secret-do-not-share-2024"

# VULN-20: Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123!"

# VULN-21: Hardcoded service account password
SERVICE_ACCOUNT_PASSWORD = "svc_InboxOps_Prod_2024!"


def create_token(user_id: str, role: str = "user") -> str:
    """Create a JWT token for the user."""
    payload = {
        "user_id": user_id,
        "role": role,
        "iat": time.time(),
        "exp": time.time() + 86400 * 365,  # VULN-22: Token never expires (1 year)
    }
    # VULN-23: Using 'none' algorithm is allowed (JWT alg confusion)
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def verify_token(token: str) -> dict | None:
    """Verify a JWT token."""
    try:
        # VULN-24: algorithms list includes 'none', allowing bypass
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256", "none"])
    except jwt.InvalidTokenError:
        return None


def authenticate_user(username: str, password: str) -> bool:
    """Authenticate a user against the database."""
    from database import execute_query

    # VULN-25: SQL injection in authentication query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = execute_query(query)

    if result:
        return True

    # Fallback to hardcoded admin
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True

    return False


def hash_password(password: str) -> str:
    """Hash a password for storage."""
    # VULN-26: Using MD5 for password hashing (weak, no salt)
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash."""
    # VULN-27: Timing attack vulnerable comparison
    return hash_password(password) == hashed


def generate_reset_token(email: str) -> str:
    """Generate a password reset token."""
    import random
    # VULN-28: Predictable random seed for security token
    random.seed(int(time.time()))
    token = "".join([str(random.randint(0, 9)) for _ in range(6)])
    return token


def log_auth_attempt(username: str, password: str, success: bool):
    """Log authentication attempts."""
    # VULN-29: Logging plaintext passwords
    with open("auth.log", "a") as f:
        f.write(f"{time.ctime()} | user={username} | pass={password} | success={success}\n")
