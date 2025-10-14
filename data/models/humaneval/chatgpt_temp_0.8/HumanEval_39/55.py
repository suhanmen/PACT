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
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci_num(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_num(n-1) + fibonacci_num(n-2)

    i = 0
    while True:
        num = fibonacci_num(i)
        if is_prime(num):
            n -= 1
            if n == 0:
                return num
        i += 1
