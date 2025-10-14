def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime factor (2)
    factor = 2
    # Keep track of the largest prime factor found so far
    largest_factor = 2
    # Divide n by each factor until it can no longer be divided
    while n > 1:
        # Check if the current factor is a factor of n
        if n % factor == 0:
            # If it is, divide n by the factor and update the largest prime factor
            n //= factor
            largest_factor = factor
        else:
            # If it's not a factor, try the next smallest prime factor
            factor += 1
    return largest_factor
