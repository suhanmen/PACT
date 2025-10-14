def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        """Helper function to check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # First two Fibonacci numbers
    fib = [1, 2]
    # Keep generating Fibonacci numbers until we find one that's both prime and Fibonacci
    while True:
        # Generate the next Fibonacci number
        next_fib = fib[-1] + fib[-2]
        # Check if it's prime and return it if it is, else add it to our list of Fibonacci numbers
        if is_prime(next_fib):
            if n == 1:
                return next_fib
            n -= 1
        fib.append(next_fib)
