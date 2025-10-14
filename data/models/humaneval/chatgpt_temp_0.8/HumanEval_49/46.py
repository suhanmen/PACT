def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        t = modp(n // 2, p)
        return (t * t) % p
    else:
        t = modp(n - 1, p)
        return (2 * t) % p
