def decimal_to_binary(decimal_number):
    remainders = []
    while decimal_number > 0:
        remainder = decimal_number % 2
        remainders.append(remainder)
        decimal_number = decimal_number // 2
    binary_number = ''.join(str(bit) for bit in remainders[::-1])
    return binary_number


decimal_value = 25
binary_value = decimal_to_binary(decimal_value)
print(f"The binary equivalent of {decimal_value} is {binary_value}.")
