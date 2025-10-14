def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    elif n == 1:
        return 2 % p
    elif n % 2 == 0:
        # 2^(2k) = (2^k)^2
        return modp(n // 2, p)**2 % p
    else:
        # 2^(2k+1) = 2^(2k) * 2
        return modp(n // 2, p)**2 * 2 % p
