# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        # Use the fact that (a*b) mod p = ((a mod p) * (b mod p)) mod p,
        # and that (a^2) mod p = ((a mod p)^2) mod p.
        a = modp(n // 2, p)
        return (a * a) % p
    else:
        # Use the fact that (a*b) mod p = ((a mod p) * (b mod p)) mod p,
        # and that (a^2) mod p = ((a mod p)^2) mod p.
        a = modp(n - 1, p)
        return (2 * a) % p
