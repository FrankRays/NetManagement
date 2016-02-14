from Crypto.PublicKey import RSA
from Crypto import Random


class RSAkey0(object):

    def __init__(self):
        rng = Random.new().read
        RSAkey = RSA.generate(1024, rng)
        self.privatekey = RSAkey
        self.publicKey = self.privatekey.publickey()
    
    def export_private(self):
        if self.privatekey is not None:
            return self.privatekey.exportKey()

    def export_public(self):
        return self.publicKey.exportKey()

    def encrypt_data(self, data):
        enc_data = self.publicKey.encrypt(data, 32)
        return enc_data

    def decrypt_data(self, enc_data):
        data = self.privatekey.decrypt(enc_data)
        return data

class RSAkey1(object):

    def __init__(self, publicKeyo):
        self.publicKey = publicKeyo
        self.privatekey = None
    
    def export_private(self):
        if self.privatekey is not None:
            return self.privatekey.exportKey()

    def export_public(self):
        return self.publickey.exportKey()

    def encrypt_data(self, data):
        enc_data = self.publicKey.encrypt(data, 32)
        return enc_data

    def decrypt_data(self, enc_data):
        data = self.privatekey.decrypt(enc_data)
        return data

class RSAkey2(object):

    def __init__(self, privateKey, publicKey):
        self.privatekey = privateKey
        self.publicKey = publicKey
    
    def export_private(self):
        if self.privatekey is not None:
            return self.privatekey.exportKey()

    def export_public(self):
        return self.publickey.exportKey()

    def encrypt_data(self, data):
        enc_data = self.publicKey.encrypt(data, 32)
        return enc_data

    def decrypt_data(self, enc_data):
        data = self.privatekey.decrypt(enc_data)
        return data

def import_key(exportedkey):
    return RSA.importKey(exportedkey)

def generate_public(privatekey):
    return privatekey.publickey()

"""
r = RSAkey0()
r1 = RSAkey1(r.publicKey)
r2 = RSAkey2(r.privatekey, r.publicKey)
st11 = "hello"
e = r1.encrypt_data(st11)
print e
d = r2.decrypt_data(e)
print d
"""
