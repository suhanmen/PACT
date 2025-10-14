def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # start with the smallest prime factor, which is 2
    factor = 2
    
    # keep trying larger factors until we find the largest prime factor
    while n > factor:
        if n % factor == 0:
            # if the factor divides n, then divide n by the factor
            n = n // factor
        else:
            # if the factor doesn't divide n, try the next largest factor
            factor += 1
    
    # the largest factor at this point is the largest prime factor
    return factor
