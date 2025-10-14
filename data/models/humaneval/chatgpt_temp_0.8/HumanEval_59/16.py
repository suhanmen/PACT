import math

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 0
    # check for factors up to the square root of n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            # if i is a factor, check if it is prime
            is_prime = True
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                largest_factor = i
    if largest_factor == 0:
        # if no prime factor found, n itself is prime
        return n
    else:
        return largest_factor
