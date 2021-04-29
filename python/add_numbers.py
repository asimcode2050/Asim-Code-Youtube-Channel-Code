# https://youtu.be/Jwgo6kZlNQ8
def add_numbers(numbers):
    return sum(int(number)
    for number in numbers.split()
    if number.isdigit())

print(add_numbers('20 abc 30 def4'))
