def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factor = 2
    while factor <= n:
        if n % factor == 0:
            n //= factor
            # If we've found a factor, reduce n by dividing by the factor repeatedly.
            # This ensures that the next factor we find will be larger than the previous one.
            while n % factor == 0:
                n //= factor
            if n == 1:
                return factor
        factor += 1
    return factor
