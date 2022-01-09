import base64
import hashlib

from cryptography.fernet import Fernet

key = Fernet.generate_key()


def encrypt(message_text: str) -> bytes:
    key_encoded = base64.urlsafe_b64encode(key)
    f = Fernet(key)
    return f.encrypt(message_text.encode())


def decrypt(message_code: bytes) -> str:
    key_encoded = base64.urlsafe_b64encode(key)
    f = Fernet(key)
    return f.decrypt(message_code).decode()
