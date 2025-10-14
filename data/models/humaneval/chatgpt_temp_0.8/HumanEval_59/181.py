def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime factor (2)
    factor = 2
    # Keep dividing n by the current factor until it's no longer divisible
    while n % factor == 0:
        n //= factor
    # Check for other factors up to the square root of n
    limit = int(n ** 0.5) + 1
    for factor in range(3, limit, 2):
        while n % factor == 0:
            n //= factor
    # If n is still greater than 1, it means it has a prime factor greater than sqrt(n)
    if n > 1:
        return n
    # Otherwise, the largest prime factor is the last factor we checked
    return factor
