# Validating credit card numbers
def luhn_algorithm(card_number: str) -> bool:
    card_number = ''.join(filter(str.isdigit, card_number))
    digits = [int(d) for d in reversed(card_number)]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    return total % 10 == 0


def main():
    card_numbers = [
        "4532 1488 0343 6467",  # Valid Visa card
        "6011 1234 5678 9012",  # Valid Discover card
        "3782 8224 6310 005",    # Valid American Express card
        "1234 5678 9012 3456",   # Invalid card
        "4012 8888 8888 1881"    # Valid Visa card
    ]

    for card in card_numbers:
        is_valid = luhn_algorithm(card)
        print(f"Card Number: {card} - Valid: {is_valid}")

if __name__ == "__main__":
    main()
