def calculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def create_profile(**user_info):
    profile = {}  # 'profile' is initialized as an empty dictionary.
    for key, value in user_info.items():
        profile[key] = value
    return profile


numbers = [10, 20, 30, 40]
print("Sum of numbers:", calculate_sum(*numbers))
user_details = {"name": "John", "age": 30, "city": "New York"}
print("User profile:", create_profile(**user_details))
