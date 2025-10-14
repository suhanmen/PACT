# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
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
    base = 2 % p
    while n > 0:
        if n & 1:
            result = (result * base) % p
        base = (base * base) % p
        n >>= 1
    return result
