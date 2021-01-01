import math
def check_prime(num):
    if num <2:
        return False
    if num <4:
        return True
    if num % 2 == 0:
        return False

    odd_num = range(3,int(math.sqrt(num))+1,2)
    return not any(num % i == 0 for i in odd_num)
print(check_prime(4))
print(check_prime(6))
print(check_prime(9))