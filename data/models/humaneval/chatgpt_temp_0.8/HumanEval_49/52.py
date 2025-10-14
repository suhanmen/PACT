def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1 % p
    elif n % 2 == 0:  # n is even
        return modp(n//2, p)**2 % p
    else:  # n is odd
        return (2 * modp(n-1, p)) % p
