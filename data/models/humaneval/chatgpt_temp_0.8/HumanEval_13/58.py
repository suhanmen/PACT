def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of integers a and b.
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
