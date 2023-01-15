from .config import Config
from base64 import b64encode, b64decode
from cryptography.fernet import Fernet, InvalidToken
# import hashlib as hl
import time
import json

def custom_encrypt(key=Config.SECRET_KEY_AUTH, string=''):
    key = bytes(key, 'utf-8')

    fer = Fernet(key=key)
    string = fer.encrypt(data=bytes(string, 'utf-8'))
    string = b64encode(string)
    return string


def custom_decrypt(key=Config.SECRET_KEY_AUTH, string=''):
    key = bytes(key, 'utf-8')

    string = b64decode(string)
    fer = Fernet(key=key)

    try:
        string = fer.decrypt(token=string)
    except InvalidToken as e:
        raise Exception("Encryption error")
    
    string = string.decode('utf-8')
    return string

def tokenize(user):
    d = {
        'username': user.username,
        'id': user.id,
        'ttl': (time.time_ns() + (86400000000000*2))
    }
    return custom_encrypt(string=json.dumps(d)).decode('utf-8')

def detokenize(token):
    d = json.loads(custom_decrypt(string=token))
    return d

def validToken(token):
    d = detokenize(token)
    return d['ttl'] > time.time_ns()
