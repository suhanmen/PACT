# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 2 % p
    elif n % 2 == 0:
        # If n is even, compute (2^(n/2))^2 mod p
        x = modp(n // 2, p)
        return (x * x) % p
    else:
        # If n is odd, compute 2 * 2^(n-1) mod p
        x = modp(n - 1, p)
        return (2 * x) % p
