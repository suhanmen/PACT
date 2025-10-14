# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
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
        """
        is_prime checks if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Initialize the Fibonacci sequence with the first two numbers
    fib = [1, 1]
    # Use a loop to generate the Fibonacci numbers until we reach the n-th prime Fibonacci number
    while len(fib) < n:
        # Calculate the next Fibonacci number by adding the last two numbers in the sequence
        next_fib = fib[-1] + fib[-2]
        # Check if the next Fibonacci number is prime
        if is_prime(next_fib):
            fib.append(next_fib)
    # Return the n-th prime Fibonacci number
    return fib[-1]
