# CANNOT PARSE CODE SNIPPET
python
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    a, b = 0, 1
    count = 0
    while True:
        c = a + b
        a, b = b, c
        if is_prime(c):
            count += 1
            if count == n:
                return c
