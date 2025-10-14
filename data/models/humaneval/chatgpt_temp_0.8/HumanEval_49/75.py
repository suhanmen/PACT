def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        a = modp(n/2, p)
        return (a*a) % p
    else:
        return (2*modp(n-1, p)) % p
