"""
List of Prime Numbers from 1 to 100 in Python
YouTube Channel : Asim Code
https://youtu.be/5pVhuh7JYk8
"""
primes = []
limit = 100

for n in range(2,limit+1):
    isprime = True
    for divisor in range(2,n):
        if n % divisor == 0:
            isprime = False
            break
    if isprime:
        primes.append(n)
    
print(primes)
