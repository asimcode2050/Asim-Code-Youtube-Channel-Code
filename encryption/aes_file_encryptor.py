from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

def generate_key():
    return os.urandom(32)

def encrypt_file(file_name, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_name, 'rb') as file:
        file_data = file.read()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    with open(file_name + '.enc','wb') as file:
        file.write(iv + encrypted_data)
    print(f'File {file_name} encrypted to {file_name}.enc')


def decrypt_file(encrypted_file_name, key):
    with open(encrypted_file_name, 'rb') as file:
        iv = file.read(16)
        encrypted_data = file.read()
    
    cipher  = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend)
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    with open(encrypted_file_name.replace('.enc',''),'wb') as file:
        file.write(data)
    
    print(f'File {encrypted_file_name} decrypted to {encrypted_file_name.replace(".enc","")}')

if __name__ == "__main__":
        key = generate_key()
        #original_file = r"C:\asim\forensics\example.txt"
        original_file = 'example.txt'  # Replace with your file name
        encrypt_file(original_file, key)

        encrypted_file = original_file + '.enc'
        decrypt_file(encrypted_file, key)






