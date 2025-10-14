def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    base = 2 % p
    while n:
        if n & 1:
            result = (result * base) % p
        base = (base * base) % p
        n >>= 1
    return result
