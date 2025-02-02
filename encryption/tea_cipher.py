def tea_encrypt(v, key, rounds=32, delta=0x9E3779B9):
    v0, v1 = v
    k0, k1, k2, k3 = key
    sum_ = 0
    for _ in range(rounds):
        sum_ += delta
        v0 += ((v1 << 4) + k0) ^ (v1 + sum_) ^ ((v1 >> 5) + k1)
        v1 += ((v0 << 4) + k2) ^ (v0 + sum_) ^ ((v0 >> 5) + k3)
    return v0, v1
def tea_decrypt(v, key, rounds=32, delta=0x9E3779B9):
    v0, v1 = v
    k0, k1, k2, k3 = key
    sum_ = delta * rounds
    for _ in range(rounds):
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum_) ^ ((v0 >> 5) + k3)
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum_) ^ ((v1 >> 5) + k1)
        sum_ -= delta
    return v0, v1
if __name__ == '__main__':
    key = (0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210)
    plaintext = (0x12345678, 0x9ABCDEF0)
    print(f'Plaintext: {plaintext}')
    encrypted = tea_encrypt(plaintext, key)
    print(f'Encrypted: {encrypted}')
    decrypted = tea_decrypt(encrypted, key)
    print(f'Decrypted: {decrypted}')
