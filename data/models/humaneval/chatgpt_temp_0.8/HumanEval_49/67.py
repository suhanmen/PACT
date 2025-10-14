# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 2 % p
    if n % 2 == 0:
        x = modp(n//2, p)
        return (x * x) % p
    else:
        x = modp(n-1, p)
        return (2 * x) % p
