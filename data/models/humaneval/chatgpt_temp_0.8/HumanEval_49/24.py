# CANNOT PARSE CODE SNIPPET
python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n //= 2
        result = (result * result) % p
    return result
