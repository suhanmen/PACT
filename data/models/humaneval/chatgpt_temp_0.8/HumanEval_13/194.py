def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a is the greater integer
    if a < b:
        a, b = b, a
        
    while b != 0:
        # Find remainder of a/b
        remainder = a % b
        
        # Update a and b
        a = b
        b = remainder
        
    return a
