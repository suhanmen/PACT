python
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
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    fib = fibonacci()
    primes = []
    while len(primes) < n:
        x = next(fib)
        if is_prime(x):
            primes.append(x)
    return primes[-1]
