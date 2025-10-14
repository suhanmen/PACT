def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * 2) % p
        n //= 2
        x = (2 * 2) % p
    return res
