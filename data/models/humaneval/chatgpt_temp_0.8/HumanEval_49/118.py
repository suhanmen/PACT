def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n == 1:
        return 2 % p
    else:
        temp = modp(n//2, p)
        if n % 2 == 0:
            return (temp * temp) % p
        else:
            return (2 * temp * temp) % p
