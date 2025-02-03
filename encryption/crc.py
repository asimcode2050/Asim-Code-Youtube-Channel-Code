import binascii
def compute_crc32(data):
    data_bytes = data.encode()
    crc32_checksum = binascii.crc32(data_bytes) & 0xFFFFFFFF
    return crc32_checksum
def verify_crc32(data, expected_checksum):
    computed_checksum = compute_crc32(data)
    return computed_checksum == expected_checksum
if __name__ == '__main__':
    input_data = 'Hello, CRC-32!'
    checksum = compute_crc32(input_data)
    print(f'Computed CRC-32 Checksum: {checksum}')
    is_valid = verify_crc32(input_data, checksum)
    print(f'Checksum Verification: {is_valid}')
