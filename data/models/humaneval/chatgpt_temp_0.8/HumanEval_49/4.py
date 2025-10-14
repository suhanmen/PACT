def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1    # Start with 2^0 = 1
    for i in range(n):
        result = (result * 2) % p    # Compute 2^i mod p using modular exponentiation
    return result
