def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime factor
    factor = 2
    
    # Keep dividing n by the smallest prime factor until it's no longer divisible
    while n % factor == 0:
        n //= factor
    
    # Move on to the next prime factor
    factor = 3
    
    # Keep dividing n by prime factors until we reach the largest one
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 2
    
    # If n is still greater than the largest prime factor found so far, it must be prime
    return n
