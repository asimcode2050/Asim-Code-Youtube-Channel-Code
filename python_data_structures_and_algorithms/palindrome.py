def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1  # Increment 'n' by 1 after each check if it is not a palindrome
    return n

input_number = 123
result = next_palindrome(input_number)
print(f"The smallest palindrome greater than {input_number} is {result}")
