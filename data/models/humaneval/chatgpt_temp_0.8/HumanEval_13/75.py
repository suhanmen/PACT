def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a is greater than b
    if b > a:
        a, b = b, a
    
    # Iterate through possible divisors from 1 to b
    for divisor in range(1, b+1):
        # Check if divisor divides both a and b
        if a % divisor == 0 and b % divisor == 0:
            gcd = divisor
    
    return gcd
