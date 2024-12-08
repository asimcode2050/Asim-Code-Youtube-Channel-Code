'''
For example, if you shift the letters by 3 positions:
A becomes D
B becomes E
C becomes F
and so on...
'''
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message


def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message


plaintext = "Hello World!"
shift = 3
encrypted_message = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted Message:", encrypted_message)
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)
