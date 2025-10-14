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
    if n == 1:
        return 2
    
    # Initialize our list of Fibonacci numbers with the first two numbers
    fibs = [0, 1]
    
    # Keep generating Fibonacci numbers until we find one that is both prime and in our list
    while len(fibs) < n:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
        
        # Check if the current Fibonacci number is prime
        is_prime = True
        for i in range(2, int(next_fib ** 0.5) + 1):
            if next_fib % i == 0:
                is_prime = False
                break
        
        # If the current Fibonacci number is prime, return it
        if is_prime and next_fib not in fibs:
            return next_fib
