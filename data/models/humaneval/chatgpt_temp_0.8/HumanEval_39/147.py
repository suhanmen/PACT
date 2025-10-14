def is_prime(num):
    """
    Helper function that checks if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None
    fib_1, fib_2 = 1, 1
    for i in range(n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        while not is_prime(fib_1):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_1
