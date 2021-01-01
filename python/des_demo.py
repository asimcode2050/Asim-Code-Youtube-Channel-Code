from Crypto.Cipher import DES
password = "password"
cipher = DES.new('mycipher')
enc_pass = cipher.encrypt(password)
print("Encrypted pass: "+str(enc_pass))
cipher = DES.new('mycipher')
decrypt_pass = cipher.decrypt(enc_pass)
print("Decrypted pass: "+str(decrypt_pass))
