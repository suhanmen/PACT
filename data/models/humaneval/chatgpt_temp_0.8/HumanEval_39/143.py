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
    def is_prime(num: int) -> bool:
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize the first two Fibonacci numbers
    fib1, fib2 = 0, 1

    # Keep track of the index and the current Fibonacci number
    index = 1
    fib_num = fib2

    # Loop until we find the n-th prime Fibonacci number
    while True:
        # Check if the current Fibonacci number is prime
        if is_prime(fib_num):
            # If it is, increment the index
            index += 1
            # If we've found the n-th prime Fibonacci number, return it
            if index == n+1:
                return fib_num
        # Compute the next Fibonacci number and update the variables
        fib1, fib2 = fib2, fib1 + fib2
        fib_num = fib2
