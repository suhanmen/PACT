# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize the first two Fibonacci numbers:
    fib_1 = 1
    fib_2 = 1
    # Keep track of the current number and its index:
    current = 1
    index = 2  # We start at index 2 because fib_2 is the second Fibonacci number
    # Loop until we find the n-th number that is a prime Fibonacci number:
    while True:
        # Compute the next Fibonacci number:
        fib_next = fib_1 + fib_2
        # Check if it's prime:
        if is_prime(fib_next):
            current = fib_next
            index += 1
            if index > n:
                break
        # Update the Fibonacci sequence:
        fib_1 = fib_2
        fib_2 = fib_next
    return current
