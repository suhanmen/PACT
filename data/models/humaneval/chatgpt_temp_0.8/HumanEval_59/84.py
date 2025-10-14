import math

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the smallest prime factor of n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            # If i is a factor of n, divide n by i, and look for the largest prime factor of the result
            return largest_prime_factor(n // i)
    # If no prime factor was found, n must be the largest prime factor itself
    return n
