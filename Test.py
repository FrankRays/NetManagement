__author__ = 'Hadar'
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import win32api
import ctypes
import win32con
class AESCipher(object):
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
a = AESCipher("Hello")
b = AESCipher("Hello")
e1 = a.encrypt("Hadar")
e2 = b.encrypt("Hadar")
print e1
print e2
d1 = a.decrypt(e2)
d2 = b.decrypt(e2)
print d1
print d2
print win32api.GetCursorPos()
print win32api.GetUserName()
#print win32api.GetComputerObjectName(win32con.ComputerName)
print win32api.GetDiskFreeSpace()


def get_open_programs():
        #Returns a list that contains the titles of the open programms that are shown.
        enumwindows = ctypes.windll.user32.EnumWindows  # Filters all opened windows
        enumwindowsproc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),
                                             ctypes.POINTER(ctypes.c_int))
        GetWindowText = ctypes.windll.user32.GetWindowTextW  # Gets programs's title
        GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW  # Gets the exact title of the buffer size
        IsWindowVisible = ctypes.windll.user32.IsWindowVisible  # shows only the visible ones

        titles = []

        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                titles.append(buff.value)
            return True

        enumwindows(enumwindowsproc(foreach_window), 0)  # Callback
        return titles
titles = get_open_programs()
for title in titles:
    print title

def get_registry_value(key, subkey, value):
    import _winreg
    key = getattr(_winreg, key)
    handle = _winreg.OpenKey(key, subkey)
    (value, type) = _winreg.QueryValueEx(handle, value)
    return value

def get_cpu_model():
        #Returns computer's CPU model
        return get_registry_value("HKEY_LOCAL_MACHINE","HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0","ProcessorNameString")
print get_cpu_model()
