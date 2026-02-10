"""
InboxOps File Handler
=====================
File upload/download and processing utilities.
"""
import os
import yaml

def read_file(filepath: str) -> str:
    # VULN-51: Path traversal - no sanitization of user-provided path
    with open(filepath, "r") as f:
        return f.read()

def save_upload(filename: str, content: bytes) -> str:
    # VULN-52: Path traversal in file upload, no extension validation
    upload_dir = "/tmp/uploads"
    os.makedirs(upload_dir, exist_ok=True)
    path = os.path.join(upload_dir, filename)
    with open(path, "wb") as f:
        f.write(content)
    return path

def load_config_yaml(yaml_string: str) -> dict:
    # VULN-53: Unsafe YAML loading allows arbitrary code execution
    return yaml.load(yaml_string, Loader=yaml.FullLoader)

def list_directory(path: str) -> list:
    # VULN-54: Directory listing without access control
    return os.listdir(path)
