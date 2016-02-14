from Crypto.Cipher import AES
import base64
import sys
#creating a pad and unpad functions in lambda design
# the byte length for the encrypted data
BS = 16

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher(object):
    """
    this class creates a chiper for AES encryption. it recieves a string that will be used as a key
    """
    def __init__( self, key ):
        self.key = key
        self.chiper = Aes.new( self.key, AES.MODE_EBC, iv)
        
    def encrypt( self, raw ):
        #the pad function is used to length the string so it could be encrypted by the AES function
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        # the func returns the string encrypted withe AEs cipher and encoded with base64
        return base64.b64encode( iv + self.cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        #remove the decodeing
        enc = base64.b64decode(enc)
        iv = enc[:16]
        return unpad(self.cipher.decrypt( enc[16:] ))
