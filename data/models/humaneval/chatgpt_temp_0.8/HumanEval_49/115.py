# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n //= 2
        squared = (2 ** 2) % p
        p_power = p
        while p_power > squared:
            p_power = (p_power ** 2) % p
        squared = (squared ** 2) % p
        result = (result * p_power) % p
    return result
