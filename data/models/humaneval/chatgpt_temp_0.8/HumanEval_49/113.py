# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 2 % p
    half = modp(n // 2, p)
    if n % 2 == 0:
        return (half * half) % p
    else:
        return (2 * half * half) % p
