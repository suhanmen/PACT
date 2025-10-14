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
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n //= 2
        p_mod = p % 2
        if p_mod == 0:
            raise ValueError("modulus p must be odd")
        result = pow(result, p-1, p)
    return result
