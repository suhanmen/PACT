from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    primes = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primes.append(d)
            n //= d
        d += 1
    if n > 1:
        primes.append(n)
    return primes
