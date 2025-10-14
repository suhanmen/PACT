# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 2 % p
    else:
        t = modp(n // 2, p)
        if n % 2 == 0:
            return (t * t) % p
        else:
            return (2 * t * t) % p
