def is_prime(n):
    """
    Return True if a given number is prime, and False otherwise.

    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:   # 1 is not prime and negative numbers can't be prime
        return False
    for i in range(2, int(n**0.5) + 1):   # check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True
