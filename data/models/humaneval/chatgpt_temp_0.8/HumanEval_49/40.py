def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    res = 2
    for i in range(n-1):
        res = res * 2 % p
    return res
