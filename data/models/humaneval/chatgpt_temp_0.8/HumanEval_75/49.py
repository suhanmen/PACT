def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise."""
    primes = []
    for i in range(2, a + 1):
        if is_prime(i):
            primes.append(i)
    if len(primes) < 3:
        return False
    for i in range(len(primes) - 2):
        for j in range(i + 1, len(primes) - 1):
            for k in range(j + 1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False
