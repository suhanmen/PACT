python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:  # check up to the square root of n
        if n % i == 0:
            n //= i  # divide n by i
        else:
            i += 1  # try the next number
    return n
