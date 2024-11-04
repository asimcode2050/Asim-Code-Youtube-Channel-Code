# Encryption and Decryption System
from cryptography.fernet import Fernet


class EncryptionSystem:
    def __init__(self):
        self.key = Fernet.generate_key()  # Generate a new key
        self.cipher = Fernet(self.key)

    def encrypt_message(self, message: str) -> bytes:
        encrypted_message = self.cipher.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message: bytes) -> str:
        decrypted_message = self.cipher.decrypt(encrypted_message).decode()
        return decrypted_message


def main():
    system = EncryptionSystem()  # Create an instance of the EncryptionSystem
    message = input("Enter the message to encrypt: ")
    encrypted_message = system.encrypt_message(message)
    print(f'Encrypted message: {encrypted_message}')
    decrypted_message = system.decrypt_message(encrypted_message)
    print(f'Decrypted message: {decrypted_message}')


if __name__ == "__main__":
    main()
