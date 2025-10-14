def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # find smallest factor of n using trial division
    factor = 2
    while factor <= n:
        if n % factor == 0:
            # n is divisible by factor; update n and try again
            n //= factor
        else:
            # factor is not a factor of n; try the next odd number
            factor += 1 if factor == 2 else 2
    return factor
