# CANNOT PARSE CODE SNIPPET
python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        m = modp(n//2, p)
        return (m * m) % p
    else:
        m = modp(n-1, p)
        return (2 * m) % p
