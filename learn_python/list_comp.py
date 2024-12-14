''' [expression for item in iterable if condition] '''
squares_of_even_numbers = [
    number ** 2 for number in range(10) if number % 2 == 0]
print(squares_of_even_numbers)  # Output: [0, 4, 16, 36, 64]
