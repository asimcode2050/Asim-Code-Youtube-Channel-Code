import hashlib
import random

class DataAnonymizer:
    def __init__(self):
        self.pseudonyms = {}  # Store pseudonyms for names

    def anonymize_name(self, name: str) -> str:
        if name not in self.pseudonyms:
            pseudonym = f"User{random.randint(1000, 9999)}"
            self.pseudonyms[name] = pseudonym
        return self.pseudonyms[name]

    def hash_email(self, email: str) -> str:
        return hashlib.sha256(email.encode()).hexdigest()

    def anonymize_data(self, data: list) -> list:
        anonymized_data = []
        for entry in data:
            anonymized_entry = {
                'name': self.anonymize_name(entry.get('name', '')),
                'email': self.hash_email(entry.get('email', '')),
            }
            anonymized_data.append(anonymized_entry)
        return anonymized_data


def main():
    data = [
        {'name': 'Alice Smith', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'email': 'bob@example.com'},
        {'name': 'Alice Smith', 'email': 'alice.smith@example.com'},
    ]

    anonymizer = DataAnonymizer()  # Create an instance of DataAnonymizer
    anonymized_data = anonymizer.anonymize_data(data)  # Anonymize the data

    print("Original Data:")
    for entry in data:
        print(entry)

        print("\nAnonymized Data:")
        for entry in anonymized_data:
            print(entry)

if __name__ == "__main__":
    main()
              
