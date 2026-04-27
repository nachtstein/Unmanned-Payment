import hashlib
def encrypt_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
