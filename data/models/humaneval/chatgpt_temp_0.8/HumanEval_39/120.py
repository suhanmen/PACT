# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 1, 1
    count = 1
    while True:
        c = a + b
        if is_prime(c):
            count += 1
            if count == n:
                return c
        a, b = b, c
