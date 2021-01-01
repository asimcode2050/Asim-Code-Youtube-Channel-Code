from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
print("Key: "+str(cipher))
text = b"Secret data"
enc_text = cipher.encrypt(text)
plain_text = cipher.decrypt(enc_text)
print("Encrypted: "+str(enc_text))
print("Decrypted: "+str(plain_text))


