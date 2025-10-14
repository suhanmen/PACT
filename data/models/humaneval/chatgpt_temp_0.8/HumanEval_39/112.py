python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    count = 2
    a, b = 2, 3
    while True:
        c = a + b
        if is_prime(c):
            count += 1
            if count == n:
                return c
        a, b = b, c
