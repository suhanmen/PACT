# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        # If n is even, use the identity (a * b) % p = ((a % p) * (b % p)) % p
        # to reduce the problem to half the size.
        m = modp(n // 2, p)
        return (m * m) % p
    else:
        # If n is odd, use the identity 2^n = 2^(n-1) * 2 to reduce the problem
        # to half the size.
        m = modp(n - 1, p)
        return (2 * m) % p
