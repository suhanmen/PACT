def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Find the smaller number between a and b
    if a < b:
        smaller = a
    else:
        smaller = b

    # Initialize the gcd to 1
    gcd = 1
    
    # Loop through all the possible common divisors between a and b
    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    
    # Return the gcd
    return gcd
