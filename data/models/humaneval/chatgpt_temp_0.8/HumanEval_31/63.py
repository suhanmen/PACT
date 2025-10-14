from math import sqrt

def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
