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
    if n < 1:
        return None

    # First two fibonacci numbers
    fib = [1, 1]

    # Loop to find nth fibonacci number
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    # Check if each fibonacci number is prime until we find the nth prime fibonacci number
    prime_fib = None
    i = 0
    while prime_fib is None:
        if is_prime(fib[i]):
            prime_fib = fib[i]
        else:
            i += 1

    return prime_fib

