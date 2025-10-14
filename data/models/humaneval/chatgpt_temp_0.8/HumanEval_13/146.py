def greatest_common_divisor(a: int, b: int) -> int:
    """ Return greatest common divisor of two integers a and b
    using Euclidean algorithm """
    while b:
        a, b = b, a % b
    return a
