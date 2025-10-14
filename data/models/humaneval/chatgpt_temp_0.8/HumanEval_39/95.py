python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    a, b = 1, 1
    count = 0
    while count < n:
        c = a + b
        a, b = b, c
        if is_prime(c):
            count += 1
            if count == n:
                return c
    return None
