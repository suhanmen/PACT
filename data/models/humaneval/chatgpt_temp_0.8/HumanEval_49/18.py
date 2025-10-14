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
    if n == 0:
        return 1
    elif n % 2 == 0:
        m = modp(n // 2, p)
        return (m ** 2) % p
    else:
        m = modp(n // 2, p)
        return (2 * m ** 2) % p
