def modp(n: int, p: int):
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
        # If n is even, use the formula (a^2) % m = ((a % m)*(a % m)) % m
        # recursively to calculate (2^n) % p
        power = modp(n//2, p)
        return (power*power) % p
    else:
        # If n is odd, use the formula (a*b) % m = ((a % m)*(b % m)) % m
        # and the fact that 2^n = 2^(n-1) * 2 to calculate (2^n) % p
        power = modp((n-1)//2, p)
        return (2*power*power) % p
