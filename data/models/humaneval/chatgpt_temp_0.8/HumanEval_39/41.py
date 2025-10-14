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
    # Initialize variables to keep track of the previous two Fibonacci numbers
    prev = 1
    curr = 1
    
    # Keep track of the current position in the Fibonacci sequence and the number of prime Fibonacci numbers found
    pos = 2
    prime_count = 0
    
    while prime_count < n:
        # Calculate the next Fibonacci number
        next_num = prev + curr
        
        # Check if the next Fibonacci number is prime
        if is_prime(next_num):
            prime_count += 1
            
            # Check if this is the n-th prime Fibonacci number
            if prime_count == n:
                return next_num
        
        # Update the previous two Fibonacci numbers
        prev = curr
        curr = next_num
        
        # Update the position in the Fibonacci sequence
        pos += 1
        
