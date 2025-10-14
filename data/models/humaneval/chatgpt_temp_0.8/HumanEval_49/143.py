# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    elif n % 2 == 0:
        # if n is even, compute (2^(n/2))^2 mod p instead
        x = modp(n // 2, p)
        return (x * x) % p
    else:
        # if n is odd, compute 2 * (2^(n-1)) mod p instead
        x = modp(n - 1, p)
        return (2 * x) % p
