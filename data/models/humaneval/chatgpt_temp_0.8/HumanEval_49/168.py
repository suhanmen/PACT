def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1 % p
    elif n % 2 == 0:
        r = modp(n//2, p)
        return (r*r) % p
    else:
        return (2*modp(n-1, p)) % p
