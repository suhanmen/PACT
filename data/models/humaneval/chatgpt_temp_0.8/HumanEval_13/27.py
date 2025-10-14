def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if a or b is 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Find the smaller number between a and b
    smaller = min(a, b)
    
    # Find the greatest common divisor by checking all numbers from 1 up to the smaller number
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    return gcd
