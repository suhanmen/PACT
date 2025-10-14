def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2 # start with the smallest prime factor
    while i <= n / i: # iterate up to the square root of n
        if n % i == 0:
            n //= i # divide n by i to reduce it
        else:
            i += 1 # if i is not a factor, try the next one
    return n
