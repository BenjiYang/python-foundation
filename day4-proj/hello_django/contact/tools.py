import hashlib


def gen_password(password):
    if isinstance(password, str):
        sha512 = hashlib.sha512()
        sha512.update(password.encode('utf-8'))
        return sha512.hexdigest()
