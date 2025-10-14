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
        helper function to check if a number is prime
        """
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    fib = [0, 1, 1]
    i = 3
    while True:
        # generate next Fibonacci number
        next_fib = fib[i-1] + fib[i-2]
        if is_prime(next_fib):
            n -= 1
        if n == 0:
            return next_fib
        fib.append(next_fib)
        i += 1
