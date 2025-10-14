def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    bin_n = bin(n)[2:]

    for char in bin_n:
        result = (result * result) % p
        if char == '1':
            result = (result * 2) % p

    return result
