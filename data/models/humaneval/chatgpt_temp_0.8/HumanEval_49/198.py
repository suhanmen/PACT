def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    """
    if n == 0:
        return 1
    elif n == 1:
        return 2 % p
    else:
        res = modp(n // 2, p) ** 2 % p
        if n % 2 == 1:
            res = res * 2 % p
        return res
