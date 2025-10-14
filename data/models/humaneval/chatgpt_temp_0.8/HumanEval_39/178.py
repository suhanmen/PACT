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
    def is_prime(n: int) -> bool:
        """Returns True if n is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

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
