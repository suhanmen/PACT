def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n-1) + fibonacci(n-2)

    i = 0
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            n -= 1
            if n == 0:
                return fib
        i += 1
