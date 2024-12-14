def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    result = numerator / denominator
    return result


try:
    print(divide_numbers(10, 2))  # Function call with valid inputs
    print(divide_numbers(10, 0))
except ValueError as e:
    print(f"Error: {e}")
