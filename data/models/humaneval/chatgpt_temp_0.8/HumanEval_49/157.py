# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n //= 2
        power = 2
        while power <= n:
            power *= 2
            square = (power % p) * (power % p) % p
        result = (result * square) % p
    return result
