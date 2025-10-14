python
from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    # Divide the number by 2 until it is no longer divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Divide the number by odd numbers until it is no longer divisible by them
    i = 3
    while i <= n**0.5:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 2
    # If n is still greater than 2, it must be a prime number
    if n > 2:
        factors.append(n)
    return factors
