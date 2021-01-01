from Crypto.PublicKey import RSA
key = RSA.generate(2048)
p_key = key.publickey().exportKey("PEM")
priv_key = key.exportKey("PEM")
print(p_key)
print(priv_key)