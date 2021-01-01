import os
import base64
import pyperclip
password = base64.b64encode(os.urandom(64)).decode('utf-8')
pyperclip.copy(password)
print(pyperclip.paste())
