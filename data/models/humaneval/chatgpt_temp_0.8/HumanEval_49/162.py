def modp(n: int, p: int):
    if n == 0:
        return 1
    # Compute 2^n using the binary expansion of n
    res = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            res = (res * base) % p
        base = (base * base) % p
        n //= 2
    return res
