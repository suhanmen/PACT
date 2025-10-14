def modp(n: int, p: int):
    if n == 0:
        return 1
    x = 2 % p
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * x) % p
        x = (x * x) % p
        n //= 2
    return res
