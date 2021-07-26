from hashlib import sha256
from pathlib import Path

import os

class Key(object):

    def __init__(self, key: str):
        self.key = sha256(key.encode('utf-8')).digest()

    def fcrypt(self, path: str, out: str = None, rename: str = None):
        """Encrypt and decrypt any file with your key."""
        file_size = Path(path).stat().st_size
        with open(path, 'rb') as f:
            crypted_lines = [bytes([ord(v) ^ self.key[i % len(self.key)]]) for i, v in enumerate([f.read(1) for _ in range(file_size)])]
        if out:
            path = out
        with open(path, 'wb') as exit_file:
            exit_file.writelines(crypted_lines)
        if rename:
            os.rename(path, rename)