def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        # 2^0 is always 1
        return 1
    # Use modulus operator to avoid large intermediate values
    result = 1
    power = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * power) % p
        power = (power * power) % p
        n = n // 2
    return result
