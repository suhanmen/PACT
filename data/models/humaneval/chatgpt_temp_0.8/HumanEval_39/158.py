def is_prime(num: int) -> bool:
    """
    Returns True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        i = 3
        a, b = 1, 1
        while i <= n:
            c = a + b
            a = b
            b = c
            if is_prime(c):
                i += 1
        return c
