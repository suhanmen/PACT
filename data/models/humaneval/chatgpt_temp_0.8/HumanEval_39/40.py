# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    if n == 1:
        return 2
    elif n == 2:
        return 3

    a, b = 2, 3
    count = 2
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1

    return b
