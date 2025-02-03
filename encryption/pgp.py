from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
def generate_pgp_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key
def pgp_encrypt(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message
def pgp_decrypt(private_key, encrypted_message):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message
if __name__ == '__main__':
    private_key, public_key = generate_pgp_key_pair()
    message = 'This is a PGP encrypted message!'
    encrypted_message = pgp_encrypt(public_key, message)
    decrypted_message = pgp_decrypt(private_key, encrypted_message)
    print(f'Encrypted Message: {binascii.hexlify(encrypted_message).decode()}')
    print(f'Decrypted Message: {decrypted_message}')
