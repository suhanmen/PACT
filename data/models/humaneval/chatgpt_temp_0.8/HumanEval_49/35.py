# CANNOT PARSE CODE SNIPPET
python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        # use the fact that (a * b) % p = ((a % p) * (b % p)) % p
        # to reduce the problem to half the size
        half = modp(n // 2, p)
        return (half * half) % p
    else:
        # use the fact that (a + b) % p = ((a % p) + (b % p)) % p
        # to reduce the problem to half the size, plus one extra power of 2
        half = modp(n // 2, p)
        return (2 * half * half) % p
