def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(x: int) -> bool:
        """
        Helper function that returns True if x is prime, False otherwise.
        """
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    # Initialize variables for the first two Fibonacci numbers
    a, b = 1, 1
    # Initialize a counter for the n-th prime Fibonacci number
    count = 0
    # Loop until we find the n-th prime Fibonacci number
    while count < n:
        # Compute the next Fibonacci number
        c = a + b
        # Check if the next Fibonacci number is prime
        if is_prime(c):
            count += 1
            # If we found the n-th prime Fibonacci number, return it
            if count == n:
                return c
        # Update the variables for the next iteration
        a, b = b, c
    # If we d
