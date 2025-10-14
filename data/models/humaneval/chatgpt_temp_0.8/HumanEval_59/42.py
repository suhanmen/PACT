def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    factor = 2
    while factor <= n / factor:
        # check if factor is a divisor of n
        if n % factor == 0:
            # recursively find the largest prime factor of n // factor
            return largest_prime_factor(n // factor)
        # increment factor
        factor += 1
    # n is prime
    return n
