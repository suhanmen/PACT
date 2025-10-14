def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        x = modp(n/2, p)
        return (x * x) % p
    else:
        x = modp(n-1, p)
        return (2 * x) % p
