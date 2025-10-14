def modp(n: int, p: int):
    if n == 0:
        return 1
    elif n == 1:
        return 2 % p
    else:
        x = modp(n // 2, p)
        if n % 2 == 0:
            return (x * x) % p
        else:
            return (2 * x * x) % p
