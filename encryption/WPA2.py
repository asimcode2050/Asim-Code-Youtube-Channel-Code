import hashlib
import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
def compute_ptk(psk, ssid, client_mac, ap_mac):
    ptk_input = psk.encode() + ssid.encode() + client_mac.encode() + ap_mac.encode()
    ptk = hashlib.pbkdf2_hmac('sha1', ptk_input, b'WPA2', 4096, dklen=64)
    return ptk
def generate_aes_key(ptk):
    aes_key = ptk[:16]
    return aes_key
def encrypt_data(aes_key, data):
    iv = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    data_bytes = data.encode()
    padded_data = data_bytes + b' ' * (16 - len(data_bytes) % 16)
    ciphertext = cipher.encrypt(padded_data)
    return iv + ciphertext
def calculate_mic(data, aes_key):
    data_bytes = data.encode()
    mic = hashlib.sha1(aes_key + data_bytes).digest()[:8]
    return mic
if __name__ == '__main__':
    ssid = 'MyWiFiNetwork'
    psk = 'SuperSecretPassword'
    client_mac = '00:11:22:33:44:55'
    ap_mac = '66:77:88:99:AA:BB'
    ptk = compute_ptk(psk, ssid, client_mac, ap_mac)
    aes_key = generate_aes_key(ptk)
    data = 'This is a WPA2 encrypted message!'
    encrypted_data = encrypt_data(aes_key, data)
    mic = calculate_mic(data, aes_key)
    print(f'Encrypted Data: {binascii.hexlify(encrypted_data).decode()}')
    print(f'MIC: {binascii.hexlify(mic).decode()}')
