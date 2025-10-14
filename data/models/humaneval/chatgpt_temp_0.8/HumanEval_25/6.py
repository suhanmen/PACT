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
    # divide by 2 until the quotient is odd or the number is 1
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # check for factors from 3 to the square root of n
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # if n is a prime greater than 2, append it to the factors list
    if n > 2:
        factors.append(n)
    return factors
