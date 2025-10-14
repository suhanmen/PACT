def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        # if n is even, use (2^(n/2))^2 = 2^n
        return modp(n//2, p)**2 % p
    else:
        # if n is odd, use 2^n = 2^(n-1) * 2
        return (2 * modp(n-1, p)) % p
