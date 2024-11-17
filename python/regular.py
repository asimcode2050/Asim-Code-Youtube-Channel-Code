import re  # Import the regular expression module
text = "My email is example@mail.com, and my phone number is 123-456-7890."
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\d{3}-\d{3}-\d{4}"
email_match = re.search(email_pattern, text)
phone_match = re.search(phone_pattern, text)
if email_match:
    print(f"Found email: {email_match.group()}")
else:
    print("No email found.")
if phone_match:
    print(f"Found phone number: {phone_match.group()}")
else:
    print("No phone number found.")
