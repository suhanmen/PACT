# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    result = 1
    power = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * power) % p
        power = (power * power) % p
        n //= 2
    return result
