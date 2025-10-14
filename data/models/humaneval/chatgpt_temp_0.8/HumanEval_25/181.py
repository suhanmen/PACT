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

    factors = []

    # Divide by 2 until we can't anymore
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Divide by odd numbers until we reach the square root of n
    i = 3
    while i <= n**0.5:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still greater than 2, then it means it is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors
