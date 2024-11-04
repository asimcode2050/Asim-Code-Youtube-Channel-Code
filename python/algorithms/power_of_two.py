def is_power_of_two(n):
    if n <= 0:
        return False  # Powers of 2 are positive integers
    return (n & (n - 1)) == 0


print(is_power_of_two(1))  # True (2^0)
print(is_power_of_two(2))  # True (2^1)
print(is_power_of_two(3))  # False
print(is_power_of_two(4))  # True (2^2)
print(is_power_of_two(5))  # False
print(is_power_of_two(16))  # True (2^4)
print(is_power_of_two(18))  # False
