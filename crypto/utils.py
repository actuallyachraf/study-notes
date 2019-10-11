from hashlib import sha256

def sha256py(x):
    h = sha256()
    h.update(x)
    return h.digest()


