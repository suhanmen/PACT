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
    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize the first two fibonacci numbers
    fib_prev = 1
    fib_curr = 1
    count = 2

    while count < n:
        # Calculate the next fibonacci number
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

        if is_prime(fib_curr):
            count += 1

    return fib_curr
