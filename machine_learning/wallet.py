import os
import hashlib
import ecdsa
import base58


def generate_private_key():
    return os.urandom(32)


def private_key_to_public_key(private_key):
    private_key_bytes = ecdsa.SigningKey.from_string(
        private_key, curve=ecdsa.SECP256k1).verifying_key
    return private_key_bytes.to_string()


def public_key_to_address(public_key):
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    version_byte = b'\x00'
    checksum = hashlib.sha256(hashlib.sha256(
        version_byte + ripemd160_hash).digest()).digest()[:4]
    address = version_byte + ripemd160_hash + checksum
    return base58.b58encode(address).decode('utf-8')


def print_wallet_details():
    private_key = generate_private_key()
    public_key = private_key_to_public_key(private_key)
    address = public_key_to_address(public_key)
    print("Private Key:", private_key.hex())
    print("Public Key:", public_key.hex())
    print("Bitcoin Address:", address)


if __name__ == "__main__":
    print_wallet_details()
