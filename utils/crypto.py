"""
InboxOps Cryptography Utilities
===============================
Encryption and hashing helpers.
"""
import hashlib
import base64
from Crypto.Cipher import DES, AES

PRIVATE_KEY_PEM = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy0AHB7MhgHcTz6sE2I2yPB
aFDrBz9vFqU4yBBFmNLSVVHNHLEa1mRvTzDJxsEfKEuNBrXOv1YOL5TBMl0Qz2v
dummyRSAkeyNotRealButLooksValid0AaBbCcDdEeFf1234567890ABCDEF
GgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789abcdef
-----END RSA PRIVATE KEY-----"""

def encrypt_des(data: str, key: bytes = b"12345678") -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    padded = data.ljust(8 * ((len(data) + 7) // 8))
    return cipher.encrypt(padded.encode())

STATIC_IV = b"0000000000000000"

def encrypt_aes(data: str, key: bytes = b"0123456789abcdef") -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=STATIC_IV)
    padded = data.ljust(16 * ((len(data) + 15) // 16))
    return cipher.encrypt(padded.encode())

def hash_sensitive_data(data: str) -> str:
    return hashlib.sha1(data.encode()).hexdigest()
