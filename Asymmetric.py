from Crypto.PublicKey import RSA
from Crypto import Random


class RSAkey0(object):
    """
    class that creates a RSA key and all his derivitievs and functions:
    public key, encryption, decryption, export key, import key, generate public key from private etc.
    """
    def __init__(self):
        """
        this initilaize function creas the private and public key
        Return: nothing
        """
        rng = Random.new().read
        RSAkey = RSA.generate(1024, rng)
        self.privatekey = RSAkey
        self.publicKey = self.privatekey.publickey()
    
    def export_private(self):
        #return an exported value of the private key
        if self.privatekey is not None:
            return self.privatekey.exportKey()

    def export_public(self):
        # return an exported version of the public key
        return self.publicKey.exportKey()

    def encrypt_data(self, data):
        """
        the func recieves as a paramter a data to encrypt and returns it encrypted
        """
        enc_data = self.publicKey.encrypt(data, 32)
        return enc_data

    def decrypt_data(self, enc_data):
        # the func recieves an encryped data and decrypts it
        data = self.privatekey.decrypt(enc_data)
        return data

class RSAkey1(object):
    """
    this class is identical to the RSAkey0 class, just designed for recieving a public key and to surrond him by a matching class 
    """
    def __init__(self, publicKeyo):
        self.publicKey = publicKeyo
        self.privatekey = None
    
    def export_public(self):
        return self.publickey.exportKey()

    def encrypt_data(self, data):
        enc_data = self.publicKey.encrypt(data, 32)
        return enc_data

class RSAkey2(object):
    """
    this class is also identical to the first class; it is designed for recieving a pricate key, making him a public key
    by the generate public which is a static function and the init func will recieve them both.
    """
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
#function that recieves a key in exported design and returns an original type
def import_key(exportedkey):
    return RSA.importKey(exportedkey)
# a function that recieves a private key and returns a public key
def generate_public(privatekey):
    return privatekey.publickey()
# example of using this classes and some functions
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
