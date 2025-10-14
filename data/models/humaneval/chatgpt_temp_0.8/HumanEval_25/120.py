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
    i = 2 # Start with 2 because it's the smallest prime factor
    
    while i * i <= n:
        if n % i:  # If n is not divisible by i
            i += 1
        else:  # If n is divisible by i
            n //= i
            factors.append(i)
    
    if n > 1:  # If there's a prime factor greater than sqrt(n)
        factors.append(n)
    
    return factors
