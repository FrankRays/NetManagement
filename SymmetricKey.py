from Crypto.Cipher import AES
import base64
import sys
BS = 16

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    
    
    def __init__( self, key ):
        self.key = key
        self.chiper = Aes.new( self.key, AES.MODE_EBC, iv)
        
    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        return base64.b64encode( iv + self.cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        return unpad(self.cipher.decrypt( enc[16:] ))
