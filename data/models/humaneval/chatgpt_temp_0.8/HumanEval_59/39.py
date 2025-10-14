def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 2
    while largest_factor <= n / 2:
        if n % largest_factor == 0:
            n //= largest_factor
        else:
            largest_factor += 1
    return n
