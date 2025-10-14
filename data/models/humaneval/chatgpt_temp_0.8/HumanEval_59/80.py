from math import sqrt

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find and remove all factors of 2
    while n % 2 == 0:
        n //= 2

    # Check for odd prime factors up to the square root of n
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            n //= i
            largest_factor = i

    # If n is still greater than 2, it must be a prime factor
    if n > 2:
        largest_factor = n

    return largest_factor
