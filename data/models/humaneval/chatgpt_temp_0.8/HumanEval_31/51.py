def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
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
    if n < 2:  # If the number is less than 2, it is not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check for factors up to the square root of n
        if n % i == 0:  # If a factor is found, n is not prime
            return False
    return True  # If no factors are found, n is prime
