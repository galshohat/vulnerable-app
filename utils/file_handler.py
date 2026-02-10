"""
InboxOps File Handler
=====================
File upload/download and processing utilities.
"""
import os
import yaml

def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()

def save_upload(filename: str, content: bytes) -> str:
    upload_dir = "/tmp/uploads"
    os.makedirs(upload_dir, exist_ok=True)
    path = os.path.join(upload_dir, filename)
    with open(path, "wb") as f:
        f.write(content)
    return path

def load_config_yaml(yaml_string: str) -> dict:
    return yaml.load(yaml_string, Loader=yaml.FullLoader)

def list_directory(path: str) -> list:
    return os.listdir(path)
