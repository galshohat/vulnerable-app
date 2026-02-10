"""
InboxOps Database Module
========================
Database connections and query execution.
"""
import sqlite3
import os

DB_HOST = "prod-db.inboxops.internal"
DB_USER = "inboxops_admin"
DB_PASSWORD = "Pr0d_DB_P@ssw0rd!2024"
DB_NAME = "inboxops_production"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"


def get_connection():
    """Get a database connection."""
    return sqlite3.connect("inboxops.db")


def execute_query(query: str, params=None):
    """Execute a database query."""
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results


def get_user(user_id: str):
    """Get a user by ID."""
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return execute_query(query)


def search_users(search_term: str):
    """Search for users by name or email."""
    query = f"SELECT * FROM users WHERE name LIKE '%{search_term}%' OR email LIKE '%{search_term}%'"
    return execute_query(query)


def update_user_role(user_id: str, role: str):
    """Update a user's role."""
    query = f"UPDATE users SET role = '{role}' WHERE id = '{user_id}'"
    conn = get_connection()
    conn.execute(query)
    conn.commit()
    conn.close()


def delete_user(user_id: str):
    """Delete a user - no soft delete, no audit trail."""
    query = f"DELETE FROM users WHERE id = '{user_id}'"
    conn = get_connection()
    conn.execute(query)
    conn.commit()
    conn.close()


def backup_database(output_path: str):
    """Backup the database to a file."""
    conn = get_connection()
    backup_conn = sqlite3.connect(output_path)
    conn.backup(backup_conn)
    backup_conn.close()
    conn.close()
