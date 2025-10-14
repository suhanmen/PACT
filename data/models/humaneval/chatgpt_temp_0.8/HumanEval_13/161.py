def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # If a is zero, return b
    if a == 0:
        return b
    # If b is zero, return a
    if b == 0:
        return a
    # Find the gcd recursively
    return greatest_common_divisor(b, a % b)
