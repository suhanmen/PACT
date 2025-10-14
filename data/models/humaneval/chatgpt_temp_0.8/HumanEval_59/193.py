import math

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with 2 as the smallest prime factor
    largest_factor = 2
    # Divide by 2 until n is no longer divisible by 2
    while n % 2 == 0:
        n //= 2
    # Check for factors up to the square root of n
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
    # If n is prime, it will be greater than 2
    if n > 2:
        largest_factor = n
    return largest_factor
