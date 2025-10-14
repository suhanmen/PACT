def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    # compute 2^n mod p using binary exponentiation
    res = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            res = (res * base) % p
        base = (base * base) % p
        n //= 2
    return res
