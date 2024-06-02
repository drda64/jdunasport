from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(hasher, password):
    return bcrypt.checkpw(password.encode('utf-8'), hasher)
