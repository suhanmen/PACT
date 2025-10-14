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

    # Divide by 2 until it's not possible
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for odd factors
    i = 3
    while i <= n**0.5 + 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 2

    # If n is a prime number greater than 2
    if n != 1:
        factors.append(n)

    return factors
