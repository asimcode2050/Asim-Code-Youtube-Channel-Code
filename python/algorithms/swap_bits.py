# Python function that swaps all odd and even bits in a 32-bit integer
def swap_odd_even_bits(n):
    EVEN_MASK = 0xAAAAAAAA  # Mask to isolate even bits
    ODD_MASK = 0x55555555   # Mask to isolate odd bits
    even_bits = (n & EVEN_MASK) >> 1
    odd_bits = (n & ODD_MASK) << 1
    return even_bits | odd_bits


if __name__ == "__main__":
    number = 29
    swapped = swap_odd_even_bits(number)
    print(f"Original number: {number} (binary: {bin(number)})")
    print(f"Swapped number: {swapped} (binary: {bin(swapped)})")
