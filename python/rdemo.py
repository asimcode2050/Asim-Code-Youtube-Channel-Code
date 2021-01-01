import os
import base64
password=base64.b64encode(os.urandom(64)).decode('utf-8')
print(password)
