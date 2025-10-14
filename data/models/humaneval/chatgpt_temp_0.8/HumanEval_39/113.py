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
        """
        Helper function to check whether a number is prime or not.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_1 = 1
    fib_2 = 1
    count = 2
    while count < n:
        fib_next = fib_1 + fib_2
        if is_prime(fib_next):
            count += 1
        fib_1 = fib_2
        fib_2 = fib_next

    return fib_next
