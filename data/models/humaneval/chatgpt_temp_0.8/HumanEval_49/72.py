def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = modp(n/2, p)
        return (temp * temp) % p
    else:
        temp = modp((n-1)/2, p)
        return (2 * temp * temp) % p
        
