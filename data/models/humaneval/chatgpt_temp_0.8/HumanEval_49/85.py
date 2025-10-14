def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    """
    if p == 1:
        return 0
    result = 1
    n = n % (p - 1)
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
        p = (p * p) % (10**18 + 3)
    return result
