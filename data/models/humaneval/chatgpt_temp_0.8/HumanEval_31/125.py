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
    if n < 2:
        # 0, 1, and negative numbers are not prime
        return False
    elif n == 2:
        # 2 is the only even prime number
        return True
    elif n % 2 == 0:
        # other even numbers are not prime
        return False
    else:
        # check odd numbers up to the square root of n
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                # if n is divisible by i, it's not prime
                return False
        # if n is not divisible by any numbers up to its square root, it's prime
        return True
