# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 2 % p
    if n % 2 == 0:
        # compute (2^(n/2))^2 modulo p
        x = modp(n // 2, p)
        return (x * x) % p
    else:
        # compute 2 * 2^(n-1) modulo p
        x = modp(n - 1, p)
        return (2 * x) % p
