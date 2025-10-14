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
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

    a, b = 1, 1
    count = 2
    while count < n:
        c = a + b
        if is_prime(c):
            count += 1
        a, b = b, c
    return a + b if n > 1 else 2
