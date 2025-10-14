def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function to check if a number is the multiplication of three prime numbers."""
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 3:
                break
    if len(primes) < 3:
        return False
    if primes[0] * primes[1] * primes[2] == a:
        return True
    else:
        return False
