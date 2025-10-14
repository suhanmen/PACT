from math import sqrt

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
        # check if number is prime
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    fib = [0, 1]
    i = 2
    while True:
        # generate next fibonacci number
        fib.append(fib[i-1] + fib[i-2])
        # check if the number is prime
        if is_prime(fib[i]):
            n -= 1
            if n == 0:
                return fib[i]
        i += 1
