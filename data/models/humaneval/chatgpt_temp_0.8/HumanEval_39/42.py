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
        Helper function to determine whether a number is prime or not.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    # initialize variables for the first two Fibonacci numbers
    fib1 = 1
    fib2 = 1

    # loop until we reach the n-th prime Fibonacci number
    count = 0
    while count < n:
        # calculate the next Fibonacci number
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib

        # check if fib is prime
        if is_prime(fib):
            count += 1

    return fib1
