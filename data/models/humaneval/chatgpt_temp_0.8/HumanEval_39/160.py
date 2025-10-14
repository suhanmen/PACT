python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    if n <= 0:
        return None
    if n == 1:
        return 2
    a, b = 1, 1
    count = 2
    while count < n:
        c = a + b
        if is_prime(c):
            count += 1
        a, b = b, c
    return c
