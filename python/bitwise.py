# In this video we will write Python code snippet that demonstrates various bitwise operations on integer types
# Python's integers are of arbitrary precision, which means they can grow in size as needed. However, operations like shifting may produce unexpected results when dealing with large integers.
# Bitwise Operations in Python

# Initialize two integer values
a = 12  # In binary: 1100
b = 5   # In binary: 0101

# Bitwise AND operation
# The AND operation compares each bit of two numbers; if both bits are 1, the result is 1.
and_result = a & b  # In binary: 1100 & 0101 = 0100 (which is 4 in decimal)
print(f"Bitwise AND of {a} and {b}: {and_result}")

# Bitwise OR operation
# The OR operation compares each bit; if at least one bit is 1, the result is 1.
or_result = a | b   # In binary: 1100 | 0101 = 1101 (which is 13 in decimal)
print(f"Bitwise OR of {a} and {b}: {or_result}")

# Bitwise XOR operation
# The XOR operation compares each bit; if the bits are different, the result is 1.
xor_result = a ^ b  # In binary: 1100 ^ 0101 = 1001 (which is 9 in decimal)
print(f"Bitwise XOR of {a} and {b}: {xor_result}")

# Bitwise NOT operation
# The NOT operation inverts all the bits. In Python, it gives the negative of the number minus one.
not_result = ~a  # In binary: ~1100 = ...11111111111111111111111111110011 (inverts the bits)
print(f"Bitwise NOT of {a}: {not_result} (This is equivalent to -{a + 1})")

# Bitwise Left Shift operation
# The left shift operation shifts all bits to the left by the specified number of positions. It adds zeros on the right.
left_shift_result = a << 2  # Shifts 1100 left by 2: 110000 (which is 48 in decimal)
print(f"Left shift {a} by 2: {left_shift_result}")

# Bitwise Right Shift operation
# The right shift operation shifts all bits to the right by the specified number of positions.
right_shift_result = a >> 2  # Shifts 1100 right by 2: 0011 (which is 3 in decimal)
print(f"Right shift {a} by 2: {right_shift_result}")

# Summary of results
print(f"Results: AND={and_result}, OR={or_result}, XOR={xor_result}, NOT={not_result}, Left Shift={left_shift_result}, Right Shift={right_shift_result}")


