import re
def check_password_strength(password):
    if len(password) < 8:
        return "Too short"
    if not re.search("[a-z]", password):
        return "Missing lowercase letter"
    if not re.search("[A-Z]", password):
        return "Missing uppercase letter"
    if not re.search("[0-9]", password):
        return "Missing digit"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Missing special character"
    return "Strong password"


if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
