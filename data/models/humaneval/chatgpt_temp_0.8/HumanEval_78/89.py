def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def hex_key(num):
    count = 0
    primes = ['2', '3', '5', '7', 'B', 'D']
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isnumeric() and is_prime(int(digit)):
            count += 1
    return count
