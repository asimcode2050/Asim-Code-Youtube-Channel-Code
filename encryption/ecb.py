from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
def ecb_encrypt(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_text = pad(plaintext.encode(), Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext
def ecb_decrypt(ciphertext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_text, Blowfish.block_size).decode()
    return plaintext
if __name__ == '__main__':
    key = b'secretkey123456'
    plaintext = 'Hello, ECB Mode!'
    print(f'Plaintext: {plaintext}')
    encrypted = ecb_encrypt(plaintext, key)
    print(f'Encrypted: {encrypted}')
    decrypted = ecb_decrypt(encrypted, key)
    print(f'Decrypted: {decrypted}')
