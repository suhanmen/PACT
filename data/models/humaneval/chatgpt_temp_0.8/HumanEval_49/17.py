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
    if p == 1:
        return 0
    result = 1
    n = n % (p - 1)
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
        p = p % (10 ** 9 + 7)
        x = 2
        res = 1
    while p > 0:
        if p % 2 == 1:
            res = (res * x) % (10 ** 9 + 7)
        x = (x * x) % (10 ** 9 + 7)
        p = p // 2
    result = (result * res) % (10 ** 9 + 7)
    return result
