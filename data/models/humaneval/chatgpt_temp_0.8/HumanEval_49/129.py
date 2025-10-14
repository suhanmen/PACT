# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    if n == 1:
        return 2 % p
    if n % 2 == 0:
        return modp(n/2, p)**2 % p
    else:
        return 2 * modp((n-1)/2, p)**2 % p
