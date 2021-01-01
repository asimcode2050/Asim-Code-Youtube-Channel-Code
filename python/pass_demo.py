import string

alpha = string.ascii_letters + string.digits
while True:
    password = ''.join(choice(alpha) for x in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break

print(password)