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
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize variables for the first two Fibonacci numbers
    prev = 1
    curr = 2
    fib_count = 2  # We've already included the first two Fibonacci numbers

    # Loop until we've found the n-th prime Fibonacci number
    while fib_count < n:
        # Calculate the next Fibonacci number
        next_fib = prev + curr
        # Check if it's prime and if so, increment the count of prime Fibonacci numbers
        if is_prime(next_fib):
            fib_count += 1
        # Update the previous and current values for the next iteration
        prev = curr
        curr = next_fib

    return curr
