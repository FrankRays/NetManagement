from Crypto.PublicKey import RSA
from Crypto import Random
class RSAkey(object):
    def __init__(self):
        rng = Random.new().read
        RSAkey = RSA.generate(1024, rng)
        self.privatekey = RSAkey
        self.publicKey = self.privatekey.publickey()

    def __init__(self, publicKeyo):
        self.publicKey = publicKeyo
        self.privatekey = None

    def __init__(self, privateKey, publicKey):
        self.privatekey = privateKey
        self.publicKey = publicKey

    def export_private(self):
        return self.privatekey.exportKey()

    def export_public(self):
        return self.publickey.exportKey()

    def encrypt_data(self, data):
        enc_data = self.publicKey.encrypt(data, 32)
        return enc_data

    def decrypt_data(self, enc_data):
        data = self.publicKey.encrypt(enc_data, 32)
        return data


def import_public(exportedkey):
    return RSA.importKey(exportedkey)


def generate_public(privatekey):
    return privatekey.publickey()

