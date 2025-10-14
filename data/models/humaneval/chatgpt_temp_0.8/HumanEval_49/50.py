# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        # If n is even, then 2^n = (2^(n/2))^2
        t = modp(n // 2, p)
        return (t * t) % p
    else:
        # If n is odd, then 2^n = 2*2^(n-1)
        t = modp(n - 1, p)
        return (2 * t) % p
