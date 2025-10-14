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
        Returns True if a number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Starting values for the Fibonacci sequence.
    fib_minus_two, fib_minus_one = 1, 1
    current_fib = 2
    # Keep track of how many prime Fibonacci numbers we've found so far.
    prime_fib_count = 0

    while prime_fib_count < n:
        if is_prime(current_fib):
            prime_fib_count += 1
        if prime_fib_count == n:
            return current_fib
        # Update the Fibonacci sequence.
        fib_minus_two = fib_minus_one
        fib_minus_one = current_fib
        current_fib = fib_minus_two + fib_minus_one
