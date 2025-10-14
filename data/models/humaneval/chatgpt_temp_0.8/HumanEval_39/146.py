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
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib1, fib2 = 1, 1
    count = 2
    while count < n:
        next_fib = fib1 + fib2
        if is_prime(next_fib):
            count += 1
        fib1, fib2 = fib2, next_fib

    return fib2
