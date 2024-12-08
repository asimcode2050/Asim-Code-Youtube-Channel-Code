def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
        number += 1
    return number - 1

n = 6
print(f"The {n}th prime number is: {nth_prime(n)}")
