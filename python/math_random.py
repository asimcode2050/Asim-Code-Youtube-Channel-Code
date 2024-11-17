import math
import random
random_number = random.randint(1, 100)
sqrt_value = math.sqrt(random_number)
log_value = math.log10(random_number)
pi_value = math.pi
rounded_sqrt = round(sqrt_value, 2)
print(f"Random number: {random_number}")
print(f"Square root: {rounded_sqrt}")
print(f"Logarithm (base 10): {log_value}")
print(f"Pi value: {pi_value}")
