def reverse_bits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result = (result << 1) | bit  # Add the extracted bit to the result
    return bin(result)[2:].zfill(32)


print(reverse_bits(43261596))  # Example input
