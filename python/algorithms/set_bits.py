# Python function to count the number of set bits (1s) in a 32-bit integer
def count_set_bits(n):
    count = 0
    for i in range(32):  # Loop through each bit position from 0 to 31
        if (n & (1 << i)) != 0:
            count += 1  # Increment the counter if the bit is set
    return count


if __name__ == "__main__":
    number = 29
    print(f"The number of set bits in {number} is: {count_set_bits(number)}")
