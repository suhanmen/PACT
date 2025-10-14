def is_prime(n):
    """Helper function to check if a number is prime"""
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function to check if a number is the multiplication of 3 prime numbers"""
    if a == 1:
        return False
    primes = []
    for i in range(2, a+1):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 3:
                break
    if len(primes) != 3:
        return False
    if primes[0] * primes[1] * primes[2] == a:
        return True
    return False
