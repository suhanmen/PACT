def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        result = modp(n // 2, p)
        return (result * result) % p
    else:
        result = modp(n - 1, p)
        return (2 * result) % p
